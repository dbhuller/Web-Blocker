
import time
from datetime import datetime as dt

# host file path: C:\Windows\System32\drivers\etc
#host_path = 'C:\Windows\System32\drivers\etc\hosts'
host_test = 'hosts_test'
redirect = '127.0.0.1'
website_list = ['www.facebook.com', 'facebook.com', 'www.instagram.com', 'instagram.com']

while True:
    #check time
    if dt(dt.now().year, dt.now().month, dt.now().day, 16) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print('Working Hours')
        #reading and printing the file
        with open(host_test, 'r+') as file:
            content = file.read()
            for site in website_list:
                if site in content:
                    pass
                else:
                    file.write(redirect + ' ' + site+'\n')
    else:
        with open(host_test,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in website_list):
                    file.write(line)
            file.truncate()
        print('Non-Working Hours')    
    time.sleep(5)