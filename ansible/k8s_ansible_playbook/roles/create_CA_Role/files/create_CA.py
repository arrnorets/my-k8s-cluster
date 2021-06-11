#!/usr/bin/env python3

import argparse
import os
import pexpect
import sys
import time

if os.path.exists(F"{sys.argv[1]}/own_ca.key") or os.path.exists(F"{sys.argv[1]}/own_ca.crt"):
    print("CA Key and/or cert already exist.")
    sys.exit(0)

# //Start key and generation
child = pexpect.spawn ( F"openssl genrsa -out {sys.argv[1]}/own_ca.key 4096" )

time.sleep(3) # // Need to saleep a little in order to give gen command to wtite the key

child.close()

# /* END BLOCK */

# // Start cert generation
child = pexpect.spawn ( F"openssl req -x509 -new -nodes -key {sys.argv[1]}/own_ca.key -sha256 -days 7500 -out {sys.argv[1]}/own_ca.crt" )
child.expect ('Country Name \(2 letter code\) \[([-_.0-9A-Za-z ]+)?\]:')
child.sendline (F"{sys.argv[2]}")
child.expect ('State or Province Name \(full name\) \[([-_.0-9A-Za-z ]+)?\]:')
child.sendline (F"{sys.argv[3]}")
child.expect ('Locality Name \(eg, city\) \[([-_.0-9A-Za-z ]+)?\]:' )
child.sendline (F"{sys.argv[4]}")
child.expect ('Organization Name \(eg, company\) \[([-_.0-9A-Za-z ]+)?\]:')
child.sendline (F"{sys.argv[5]}")
child.expect ('Organizational Unit Name \(eg, section\) \[([-_.0-9A-Za-z ]+)?\]:')
child.sendline (F"{sys.argv[6]}")

child.expect ('Common Name \(e.g. server FQDN or YOUR name\) \[([-_.0-9A-Za-z ]+)?\]:')
child.sendline (F"{sys.argv[7]}")
child.expect ('Email Address \[([-_.@0-9A-Za-z ]+)?\]:')
child.sendline (F"{sys.argv[8]}")

time.sleep(3)

child.close()

