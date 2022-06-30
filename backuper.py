#!/usr/bin/env python3
import csv
import time
import os
from routeros_ssh_connector import MikrotikDevice

def read_data_from_csv(path):
    with open(path) as datafile:
        data={}
        data_csv=csv.reader(datafile,delimiter=',')
        for row in data_csv:
            if row[0].startswith('#'):
                pass
            else:
                data.update({row.pop(0): row})
    return data

def get_backup_from_mikrotik(ip,creds):
    backup=''
    mikrotik=MikrotikDevice()
    mikrotik.connect(ip,creds[0],creds[1])
    backup=mikrotik.send_command("/export")
    return backup

### Default paths of data
devices_path='data/devices.csv'
credentials_path='data/credentials.csv'
backups_path='backups/'
logs_path='logs/'

devices=read_data_from_csv(devices_path)
credentials=read_data_from_csv(credentials_path)

for device in devices.keys():
    backup=get_backup_from_mikrotik(devices[device][2],credentials[devices[device][3]][1:3])
    try:
        os.mkdir(backups_path+device)
    except FileExistsError:
        pass
    currentdate=time.strftime("%D")
    filename=backups_path+device+'/'+currentdate.replace('/','_')+'_'+device+'.backup'
    with open(filename,'w') as f:
        f.write(backup)