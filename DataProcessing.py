import pandas as pd
import json
import csv

savefile = './Raw Data/data/car_data.csv'
newdata = {}
with open('./Raw Data/data/car_data.json') as f:
    data = json.load(f)
    for d1 in data:
        for d2 in data[d1]:
            if d2 == 'all_features':
                newdata[d1].update({'all_features' : data[d1][d2]})
            else:
                newdata.update({d1: data[d1][d2]})

with open(savefile, 'w') as f:
    f.write('ID, ')
    for key, value in newdata['820361337'].items():
        f.write('%s, ' % key)
    f.write('\n')
    for i in newdata:
        f.write('%s, ' % i)
        for key, value in newdata[i].items():
            f.write('%s, ' % value)
        f.write('\n')

