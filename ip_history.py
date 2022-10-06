import time
import smtplib
import sys
from datetime import date
ips = {}
past=time.time()-600
past_time=time.ctime(past)
arr=past_time.split(" ")
check_time=arr[4]
today = date.today()
today_date = today.strftime("%d/%b/%Y")
fh = open("/var/log/nginx/access.log", "r").readlines()
for line in fh:
    x=line.split(" ")[3]
    x=x[1:]
    date,time=x.split(":",1)
    if date==today_date and check_time<time:
        ip = line.split(" ")[0]
        if 6 < len(ip) <=15:
            ips[ip] = ips.get(ip, 0) + 1
                
alert_list=[]
for ip in ips:
    if ips[ip]>20:
        alert_list.append(ip)

print(alert_list)       
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
if len(alert_list)>0:
    message=' '.join(map(str,alert_list))
    message=message+" These ip's accessed our server more than 20 times Please verify them" 
else:
    message='everything is fine'
server.login('rahulgangwar95363@gmail.com','cxerptopgwwnxumf')
server.sendmail('rahulgangwar95363@gmail.com','piyush.vasandani@easygov.co.in',message)
print('Mail sent')
server.quit()
    



