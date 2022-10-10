# SPF/DKIM Email Validator
This script validates SPF and DKIM headers against a raw email file. This is an example script and should not be used in a production environment.

## Installation
```bash
# Clone repo
git clone path/to/repo

# Create virtual environment
python3 -m venv /path/to/new/virtual/environment

# Activate virtual environment
source /path/to/new/virtual/environment/bin/activate

# Install requirements
pip3 install -U -r requirements.txt
```

## How to
```bash
python3 main.py -e /relative/path/to/email/file # this must be an .eml file
```

## Example Runs
```bash
# Valid example against a target ecommerce email
> python3 main.py -e ./tests/test_email_1.eml                                                                                   
top: em.target.com "v=spf1 include:cust-spf.exacttarget.com -all"
include: cust-spf.exacttarget.com "v=spf1 ip4:64.132.92.0/24 ip4:64.132.88.0/23 ip4:66.231.80.0/20 ip4:68.232.192.0/20 ip4:199.122.120.0/21 ip4:207.67.38.0/24 ip4:128.17.0.0/20 ip4:128.17.64.0/20 ip4:128.17.128.0/20 ip4:128.17.192.0/20 ip4:128.245.0.0/20 ip4:128.245.64.0/20 ip4:128.245.242.0/24 ip4:128.245.243.0/24 ip4:128.245.244.0/24 ip4:128.245.245.0/24 ip4:128.245.246.0/24 ip4:128.245.247.0/24 ip4:128.245.176.0/20 ip4:207.67.98.192/27 ip4:207.250.68.0/24 ip4:209.43.22.0/28 ip4:198.245.80.0/20 ip4:136.147.128.0/20 ip4:136.147.176.0/20 ip4:13.111.0.0/16 ip4:161.71.32.0/19 ip4:161.71.64.0/20 ip4:13.110.208.0/21 ip4:13.110.216.0/22 ip4:13.110.224.0/20 ip4:159.92.157.0/24 ip4:159.92.158.0/24 ip4:159.92.159.0/24 ip4:159.92.160.0/24 ip4:159.92.161.0/24 ip4:159.92.162.0/24 -all"
Email is ok.


# Failed example against an email from a school (Fails SPF)
> python3 main.py -e ./tests/test_email_2.eml                                                                                     
top: utfi.org "v=spf1 include:spf.protection.outlook.com include:jotform.spf.utfi.org ip4:160.36.241.233 ip4:160.36.241.238 ip4:104.130.147.202 -all"
include: spf.protection.outlook.com "v=spf1 ip4:40.92.0.0/15 ip4:40.107.0.0/16 ip4:52.100.0.0/14 ip4:104.47.0.0/17 ip6:2a01:111:f400::/48 ip6:2a01:111:f403::/49 ip6:2a01:111:f403:8000::/50 ip6:2a01:111:f403:c000::/51 ip6:2a01:111:f403:f000::/52 include:spfd.protection.outlook.com -all"
include: spfd.protection.outlook.com "v=spf1 ip4:51.4.72.0/24 ip4:51.5.72.0/24 ip4:51.5.80.0/27 ip4:20.47.149.138/32 ip4:51.4.80.0/27 ip6:2a01:4180:4051:0800::/64 ip6:2a01:4180:4050:0800::/64 ip6:2a01:4180:4051:0400::/64 ip6:2a01:4180:4050:0400::/64 -all"
include: jotform.spf.utfi.org "v=spf1 ip4:8.34.210.0/24 IP4:8.34.212.0/22 ip4:8.34.216.0/22 ip4:8.35.192.0/21 ip4:23.236.48.0/20 ip4:23.251.144.0/20 ip4:34.66.0.0/15 ip4:34.68.0.0/14 ip4:34.72.0.0/16 ip4:34.121.0.0/16 ip4:34.122.0.0/15 ip4:34.132.0.0/14 ip4:34.136.0.0/16 ip4:35.184.0.0/16 ip4:35.188.0.0/17 ip4:35.188.128.0/18 ip4:35.188.192.0/19 ip4:35.192.0.0/15 ip4:35.194.0.0/18 ip4:35.202.0.0/16 ip4:35.206.64.0/18 ip4:35.208.0.0/15 ip4:35.220.64.0/19 ip4:35.222.0.0/15 ip4:35.224.0.0/15 ip4:35.226.0.0/16 ip4:35.232.0.0/16 ip4:35.238.0.0/15 ip4:35.242.96.0/19 ip4:104.154.16.0/20 ip4:104.154.32.0/19 ip4:104.154.64.0/19 ip4:104.154.96.0/20 ip4:104.154.113.0/24 ip4:104.154.114.0/23 ip4:104.154.116.0/22 ip4:104.154.120.0/23 ip4:104.154.128.0/17 ip4:104.155.128.0/18 ip4:104.197.0.0/16 ip4:104.198.16.0/20 ip4:104.198.32.0/19 ip4:104.198.64.0/20 ip4:104.198.128.0/17 ip4:107.178.208.0/20 ip4:108.59.80.0/21 ip4:130.211.112.0/20 ip4:130.211.128.0/18 ip4:130.211.192.0/19 ip4:130.211.224.0/20 ip4:146.148.32.0/19 ip4:146.148.64.0/19 ip4:146.148.96.0/20 ip4:162.222.176.0/21 ip4:173.255.112.0/21 ip4:199.192.115.0/24 ip4:199.223.232.0/22 ip4:199.223.236.0/24 ip4:34.89.128.0/17 ip4:34.104.112.0/23 ip4:34.107.0.0/17 ip4:34.124.48.0/23 ip4:34.141.0.0/17 ip4:35.198.64.0/18 ip4:35.198.128.0/18 ip4:35.207.64.0/18 ip4:35.207.128.0/18 ip4:35.220.18.0/23 ip4:35.234.64.0/18 ip4:35.235.32.0/20 ip4:35.242.18.0/23 ip4:35.242.192.0/18 ip4:35.246.128.0/17 -all"
Email failed SPF: ('fail', 'SPF fail - not authorized')
Failed IP: 167.89.20.8
Failed Host: utfi.org
Failed From Address: utkadvancement@utfi.org
Email is not ok.


# Valid example from a yoga studio
> python3 main.py -e ./tests/test_email_3.eml 
top: mindbodyonline.com "v=spf1 include:_spf.mindbodyonline.com -all"
include: _spf.mindbodyonline.com "v=spf1 ip4:138.1.49.41 ip4:138.1.55.48 ip4:130.35.98.1 ip4:167.89.64.9 ip4:167.89.65.0 ip4:198.21.3.57 ip4:50.31.48.15 ip4:167.89.57.8 ip4:167.89.57.7 ip4:52.5.58.235 ip4:52.30.3.188 ip4:52.57.179.5 ip4:3.21.51.254 ip4:167.89.65.53 ip4:167.89.75.33 ip4:167.89.69.77 ip4:168.245.55.6 ip4:198.21.2.225 ip4:198.21.3.156 ip4:167.89.12.46 ip4:167.89.12.45 ip4:167.89.52.89 ip4:40.92.0.0/15 ip4:51.4.72.0/24 include:_spf01.mindbodyonline.com -all"
include: _spf01.mindbodyonline.com "v=spf1 ip4:51.5.72.0/24 ip4:51.5.80.0/27 ip4:51.4.80.0/27 ip4:13.54.232.50 ip4:18.141.99.34 ip4:52.62.161.51 ip4:3.105.239.52 ip4:173.203.81.82 ip4:66.48.80.0/25 ip4:147.154.9.180 ip4:166.78.68.221 ip4:167.89.46.159 ip4:167.89.65.100 ip4:167.89.74.233 ip4:167.89.75.126 ip4:167.89.75.136 ip4:167.89.75.164 ip4:72.3.185.0/24 ip4:198.37.153.12 ip4:168.245.43.49 ip4:168.245.37.83 ip4:167.89.16.163 include:_spf02.mindbodyonline.com -all"
include: _spf02.mindbodyonline.com "v=spf1 ip4:167.89.62.212 ip4:167.89.32.198 ip4:167.89.32.197 ip4:167.89.21.104 ip4:40.107.0.0/16 ip4:52.100.0.0/14 ip4:104.47.0.0/17 ip4:18.220.161.28 ip4:34.210.198.81 ip4:70.20.202.155 ip4:52.208.189.67 ip4:52.59.121.243 ip4:18.202.159.42 ip4:52.205.152.15 ip4:168.62.166.28 ip4:138.91.127.63 ip4:52.175.207.55 ip4:18.140.43.196 ip4:54.253.201.86 ip4:13.55.212.171 ip4:18.139.132.28 ip4:52.76.114.192 include:_spf03.mindbodyonline.com -all"
Email is ok.

```