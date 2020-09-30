``` 
                               ___ ____ ____ ____ _  _    _ ___   /   ___  ____ ____ ____ _   _ ___  ___
                                |  |__/ |__| |    |_/  __ |  |   /    |  \ |___ |    |__/  \_/  |__]  |
                                |  |  \ |  | |___ | \_    |  |  .     |__/ |___ |___ |  \   |   |     |

```
<h4 align="center">Track-It! Password Decrypter</h4>
<p align="center">
  <a href="https://twitter.com/sho_luv">
    <img src="https://img.shields.io/badge/Twitter-%40sho_luv-blue.svg">
    <img src="https://img.shields.io/badge/python-3+-blue.svg">
  </a>
</p>

# track-it_decrypt.py
This is a tool the decrypts Track-It passwords that are encrypted with a fixed key and IV ("NumaraIT") using the DES algorithm

## notes:
        BMC Track-It! uses the known iv and key value: 'NumaraTI'. This allows
        for decryption of the passwords from track-it!.

        also, versions up to 11.3 are vulnerable to password reset exploit

## references:
        https://www.exploit-db.com/exploits/43883
        https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-4872
        https://www.rapid7.com/db/modules/auxiliary/gather/trackit_sql_domain_creds
        https://github.com/rapid7/metasploit-framework/blob/master//modules/auxiliary/gather/trackit_sql_domain_creds.rb
        https://github.com/pedrib/PoC/tree/master/exploits/TrackPwn

## find it:
        masscan -p 9010 -oB track-it -iL range
        nmap -p 9010 --open -sV -iL range

## exploit it:
        auxiliary/gather/trackit_sql_domain_creds
        auxiliary/scanner/http/bmc_trackit_passwd_reset
        exploit/windows/http/trackit_file_upload

## decrypt password:
        This tool foo!

## Usage track-it_decrypt.py
```
./track-it_decrypt.py 

___ ____ ____ ____ _  _    _ ___   /   ___  ____ ____ ____ _   _ ___  ___
 |  |__/ |__| |    |_/  __ |  |   /    |  \ |___ |    |__/  \_/  |__]  |
 |  |  \ |  | |___ | \_    |  |  .     |__/ |___ |___ |  \   |   |     |


usage: track-it_decrypt.py [-h] [-d b64_hash] [-e cleartext]

Track-It! stores its passwords DES encryption that is then Base64ed and stored. This reverses this encryption
process when the default Track-It! key is: 'NumaraTI'

optional arguments:
  -h, --help    show this help message and exit
  -d b64_hash   Track-It Password hash.
  -e cleartext  "flag discreption"

```
## Example:
![track-it_decrypte](https://user-images.githubusercontent.com/1679089/94721903-5de8e600-030b-11eb-885a-42f9c0b8ecb6.gif)
