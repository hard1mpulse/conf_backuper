import csv
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
