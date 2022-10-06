import subprocess
import sys
import crypt
import re
user=sys.argv[1]
passwd=sys.argv[2]
def add_user(user,passwd):
    regex = re.compile('[@_!#$%^&]')
    regex1=re.compile('[0-9]')
    regex2=re.compile('[A-Z]')
    if (len(passwd)<8):
        print("please enter a valid password")
        sys.exit()
    elif (regex1.search(passwd)==None):
        print("make sure your password contains digits")
        sys.exit()
    elif (regex2.search(passwd)==None):
        print("make sure your password has capital letter in it")
        sys.exit()
    elif (regex.search(passwd)==None):
        print("make sure your password contains special character")
        sys.exit()
    else:
        try:
            encpass=crypt.crypt(passwd,"22")
            subprocess.run(['useradd','-p',encpass,user])
            subprocess.run(['chage','-M','90',user])
            print(passwd)
        except:
            print(f"failed to add the user.")
            sys.exit(1)
add_user(user,passwd)
