#!/usr/bin/env python3
import csv
import time
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

devices=read_data_from_csv(devices_path)
credentials=read_data_from_csv(credentials_path)

for device in devices.keys():
    backup=get_backup_from_mikrotik(devices[device][2],credentials[devices[device][3]][1:3])
    print(backup)
