import getopt
import sys
import re
import spf
import dkim

from email import policy
from email.parser import BytesParser

def main(argv):
    email_file_path = None
    email = None

    try:
        opts, args = getopt.getopt(argv[1:], "e:", ["email_file_path"])

    except getopt.GetoptError:
        print('Failed to parse message headers. Try again.')
        sys.exit(1)

    for opt, arg in opts:
        if opt in ('-e', '--email_file_path'):
            email_file_path = arg

    if not email_file_path:
        print('Failed to include message headers\' path (-efp). Try again.')
        sys.exit(1)

    with open(email_file_path, 'rb') as fp:
        email = BytesParser(policy=policy.default).parse(fp)

        if not email:
            print('Failed to parse email.')
            sys.exit(1)

        if validate_spf(email) and validate_dkim(fp):
            print('Email is valid')
        else:
            print('Email is invalid')


def validate_spf(email):
    """
    :param email:
    :return:
    """
    # get IP address from SPF key
    spf_key = email.get('Received-SPF')
    from_key = email.get('From')
    to_key = email.get('To')
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

    spf_resp = spf.check2(
        i=ip_address,
        s=from_address,
        h=domain
    )
    if spf_resp[0] in ['pass', 'neutral', 'unknown']:
        return True

    print(f'Email failed SPF: {spf_resp[1]}')
    return False


def validate_dkim(fp):
    """"""
    fp.seek(0)
    dkim_resp = dkim.verify(fp.read())
    return dkim_resp


if __name__ == '__main__':
    main(sys.argv)
