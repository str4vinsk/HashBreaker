#!/usr/bin/env python
# -*- coding: utf-8 -*-

import passlib.hash
import crypt
import argparse
import hashlib

banner = """
  _   _              _       ____                     _               
 | | | |  __ _  ___ | |__   | __ )  _ __  ___   __ _ | | __ ___  _ __    
 | |_| | / _` |/ __|| '_ \  |  _ \ | '__|/ _ \ / _` || |/ // _ \| '__|    
 |  _  || (_| |\__ \| | | | | |_) || |  |  __/| (_| ||   <|  __/| |       
 |_| |_| \__,_||___/|_| |_| |____/ |_|   \___| \__,_||_|\_\\___||_|   

from: Vitor Conroy AKA str4vinsk
https://github.com/str4vinsk

Hash types:
{1} MD5
{2} MD5(salt + pass)
{3} MD5(pass + salt)
{4} SHA256
{5} SHA256(salt + pass)
{6} SHA256(pass + salt)
{7} SHA512
{8} SHA512(salt + pass)
{9} SHA512(pass + salt)
"""

print(banner)
parser = argparse.ArgumentParser()


parser.add_argument('wordlist', type=str, help='Passwords wordlist')
parser.add_argument('hashlist', type=str, help='Hash list, it can be just one hash too')
parser.add_argument('mode', type=str, help='Attack mode, read the README.md file for more info')
parser.add_argument('-t', '--type', type=str, help='Hash type, look up you')
parser.add_argument('-s', '--salt', type=str, help='Salt value')

args = parser.parse_args()

salted_options = ['2', '3', '5', '6', '8', '9']

def shadow_hashing(hashes):
    for line in passwords:
        hashtype = hashes.split('$')[1]
        salt = hashes.split('$')[2]

        if (hashtype == 'apr1'):
            temphash = passlib.hash.apr_md5_crypt.hash(line, salt=salt)
        elif (hashtype == '6'):
            temphash = crypt.crypt(line, "$6${0}".format(salt))
        elif (hashtype == '1'):
            temphash = crypt.crypt(line, "$1${0}".format(salt))
        elif (hashtype == '5'):
            temphash = crypt.crypt(line, "$5${0}".format(salt))
        else:
            print("[!!] Invalid Hash.")
            exit(0)

        if (temphash == hashes):
                print("===============================================")
                print ('[+] Hash --> {0}'.format(temphash))
                print ('[+] Password --> {0}'.format(line))
                print("=============================================== \r\n")
                return

def raw_hashing(inputhash):
    for line in passwords:
        if (args.type == '1'):
            temphash = hashlib.md5(line.encode('utf-8')).hexdigest()
        elif (args.type == '2'):
            temphash = hashlib.md5(args.salt.encode('utf-8') + line.encode('utf-8')).hexdigest()
        elif (args.type == '3'):
            temphash = hashlib.md5(line.encode('utf-8') + args.salt.encode('utf-8')).hexdigest()
        elif (args.type == '4'):
            temphash = hashlib.sha256(line.encode('utf-8')).hexdigest()
        elif (args.type == '5'):
            temphash = hashlib.sha256(args.salt.encode('utf-8') + line.encode('utf-8')).hexdigest()
        elif (args.type == '6'):
            temphash = hashlib.sha256(line.encode('utf-8') + args.salt.encode('utf-8')).hexdigest()
        elif (args.type == '7'):
            temphash = hashlib.sha512(line.encode('utf-8')).hexdigest()
        elif (args.type == '8'):
            temphash = hashlib.sha512(args.salt.encode('utf-8') + line.encode('utf-8')).hexdigest()
        elif (args.type == '9'):
            temphash = hashlib.sha512(line.encode('utf-8') + args.salt.encode('utf-8')).hexdigest()
        else:
            print("[!!] Invalid hash type.")
            exit(0)

        if (temphash == inputhash):
            print("===============================================")
            print ('[+] Hash --> {0}'.format(temphash))
            print ('[+] Password --> {0}'.format(line))
            print("=============================================== \r\n")
            return

try:
    wordlistfile = open(args.wordlist, 'r')
    passwords = wordlistfile.read().split('\n')

    hashfile = open(args.hashlist, 'r')
    hasharch = hashfile.read().split('\n')
except FileNotFoundError:
    print('[!!] File not found')
    exit(0)

if (args.mode == 'raw'):
    if (args.type in salted_options and args.salt is None):
        print('You have chosen a salted hash type, please specify the salt with -s option')
        exit(0)
    for inputhash in hasharch:
        if inputhash.strip():
            raw_hashing(inputhash)
elif (args.mode == 'shadow'):
    for inputhash in hasharch:
        if inputhash.strip():
            shadow_hashing(inputhash)
else:
    print("[!!] Invalid mode, please select a valid one")

