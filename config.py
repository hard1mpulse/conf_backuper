import os
#### Configurable paths
devices_path=os.path.abspath(__file__).strip('config.py')+'data/devices.csv'
credentials_path=os.path.abspath(__file__).strip('config.py')+'data/credentials.csv'
backups_path=os.path.abspath(__file__).strip('config.py')+'backups/'
logs_path=os.path.abspath(__file__).strip('config.py')+'logs/'