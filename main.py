import getopt
import sys
import re
import spf
import dkim
import logging

from email import policy
from email.parser import BytesParser

def main(argv):
    """
    Entry point for SPF/DKIM validator

    Options:
        - [REQUIRED] -e / --email_file_path | This is the relative path to the raw email that you'd like to validate.
    """
    email_file_path = None
    email = None

    try:
        opts, args = getopt.getopt(argv[1:], "e:", ["email_file_path"])

    except getopt.GetoptError:
        print('Failed to parse email path. Try again.')
        sys.exit(1)

    for opt, arg in opts:
        if opt in ('-e', '--email_file_path'):
            email_file_path = arg

    if not email_file_path:
        print('Failed to include email path (-e). Try again.')
        sys.exit(1)

    with open(email_file_path, 'rb') as fp:
        email = BytesParser(policy=policy.default).parse(fp)

        if not email:
            print('Failed to parse email.')
            sys.exit(1)

        if validate_spf(email) and validate_dkim(fp):
            print('Email is ok.')
        else:
            print('Email is not ok.')


def validate_spf(email):
    """
    Validates that the included SPF header passes an SPF check. Uses pydns and spf library to safely make the assumption.

    :param email: email.message.EmailMessage The email to validate SPF
    :return: bool
    """

    # get IP address, from, and to headers from email
    spf_key = email.get('Received-SPF')
    from_key = email.get('From')
    to_key = email.get('To')

    # Parse headers
    if not spf_key:
        return False
    ip_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    ip_address = ip_pattern.search(spf_key).group(0)
    if not ip_address:
        return False

    email_pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    from_address = email_pattern.search(from_key).group(0)
    if not from_address:
        return False

    domain = from_address.split('@')[-1]

    to_address = email_pattern.search(to_key).group(0)
    if not to_address:
        return False

    # Run validation
    spf_resp = spf.check2(
        i=ip_address,
        s=from_address,
        h=domain,
        verbose=True,
    )

    if spf_resp[0] in ['pass', 'neutral']:
        return True

    print(f'Email failed SPF: {spf_resp}')
    print(f'Failed IP: {ip_address}')
    print(f'Failed Host: {domain}')
    print(f'Failed From Address: {from_address}')
    return False


def validate_dkim(fp):
    """
    Performs DKIM validation against raw email file

    :param fp: Raw file to be passed to `dkim.verify`, does not accept email.message.EmailMessage
    :return: bool
    """
    logger = logging.getLogger('validate_dkim')

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    logger.addHandler(ch)

    fp.seek(0)
    dkim_resp = dkim.verify(fp.read(), logger=logger)
    if not dkim_resp:
        print('Email failed DKIM')

    return dkim_resp


if __name__ == '__main__':
    main(sys.argv)
