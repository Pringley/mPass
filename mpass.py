#!/usr/bin/env python
import hmac, hashlib
from getpass import getpass
from base64 import b64encode

domain = raw_input('Domain: @')
pwd = getpass('Master Password: ')
mac = hmac.new(pwd, domain, hashlib.sha512)

print b64encode(mac.digest())[:10]
