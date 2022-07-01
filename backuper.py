#!/usr/bin/env python3
import time
import os
from functions import read_data_from_csv,get_backup_from_mikrotik
#Default paths
devices_path=os.path.abspath(__file__).strip('backuper.py')+'data/devices.csv'
credentials_path=os.path.abspath(__file__).strip('backuper.py')+'data/credentials.csv'
backups_path=os.path.abspath(__file__).strip('backuper.py')+'backups/'
logs_path=os.path.abspath(__file__).strip('backuper.py')+'logs/'

devices=read_data_from_csv(devices_path)
credentials=read_data_from_csv(credentials_path)

for device in devices.keys():
    backup=get_backup_from_mikrotik(devices[device][2],credentials[devices[device][3]][1:3])
    try:
        os.mkdir(backups_path+device)
    except (FileNotFoundError,FileExistsError):
        pass
    currentdate=time.strftime("%D")
    filename=backups_path+device+'/'+currentdate.replace('/','_')+'_'+device+'.backup'
    with open(filename,'w') as f:
        f.write(backup)