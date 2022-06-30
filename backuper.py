#!/usr/bin/env python3
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


### Default paths of data
devices_path='data/devices.csv'
credentials_path='data/credentials.csv'