import smtplib
import subprocess
import sys
import random
import crypt
user=sys.argv[1]
NumberCase="0123456789"
UpperCase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LowerCase="abcdefghijklmnopqrstuvwxyz"
SpecialCase="#@$%^&*=!"
type1=''.join(random.choice(NumberCase) for i in range(2))
type2=''.join(random.choice(UpperCase) for i in range(2))
type3=''.join(random.choice(LowerCase) for i in range(2))
type4=''.join(random.choice(SpecialCase) for i in range(2))
newpasswd=type1+type2+type3+type4
newpasswd=''.join(random.sample(newpasswd,len(newpasswd)))
enc_passwd=crypt.crypt(newpasswd,"22")
try:
    subprocess.run(['usermod','-p',enc_passwd,user])
    print(f"password changed successfully new password is:{newpasswd}")
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    message = f"Greeting of the day {user},your password has been changed and your new password is {newpasswd} \n kindly use this password for future work"
    server.login('rahulgangwar95363@gmail.com','mcfvthbwucwdxrfb')
    server.sendmail('rahulgangwar95363@gmail.com','rahul.gangwar@easygov.co.in',message)
    print('Mail sent')
    server.quit()
except:
    print("some error occured")
    sys.exit(1) 

