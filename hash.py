import passlib.hash
import crypt
import argparse


parser = argparse.ArgumentParser(description='Linux hashes breaker script')

banner = """
  _   _              _       ____                     _               
 | | | |  __ _  ___ | |__   | __ )  _ __  ___   __ _ | | __ ___  _ __    
 | |_| | / _` |/ __|| '_ \  |  _ \ | '__|/ _ \ / _` || |/ // _ \| '__|    
 |  _  || (_| |\__ \| | | | | |_) || |  |  __/| (_| ||   <|  __/| |       
 |_| |_| \__,_||___/|_| |_| |____/ |_|   \___| \__,_||_|\_\\___||_|   

Codado por: Vitor Conroy AKA str4vinsk
https://github.com/str4vinsk

Como funciona ? 
O script pega todas as hashes do arquivo mencionado e faz um processo de bruteforce
para cada uma delas, pegando cada palavra da wordlist e a criptografando de acordo com o tipo de hash,
se a hash recém criptografada for igual a hash do arquivo a senha está correta.

Supported Hashes:
{1} MD5
{2} SHA256
{3} SHA512
{4} APR1-MD5
"""

print(banner)


parser.add_argument('wordlist', type=str, help='A lista de senhas para ser testada')
parser.add_argument('hashlist', type=str, help='Lista que contém todas as hashes a serem quebradas')
parser.add_argument('-o', '--output', type=str, help='Arquivo de output')

args = parser.parse_args()

def hashing(hashes):
    for line in passwords:
        temphash = ''

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
            print("Hash inválida ou desconhecida.")
            exit(0)

        if (temphash == hashes):
                print("===============================================")
                print ('Hash --> {0}'.format(temphash))
                print ('Senha --> {0}'.format(line))
                print("=============================================== \r\n")
                return

try:
    wordlistfile = open(args.wordlist, 'r')
    passwords = wordlistfile.read().split('\n')

    hashfile = open(args.hashlist, 'r')
    hasharch = hashfile.read().split('\n')
except FileNotFoundError:
    print('Arquivo inexistente')
    exit(0)

for inputhash in hasharch:
    if inputhash.strip():
        hashing(inputhash)

wordlistfile.close()
hashfile.close()

