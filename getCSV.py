import csv
from flask import session
import datetime
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time

def getFile():
    # traigo datos del csv mas reciente
    dir_path = os.getcwd() + '/CSVFiles'
    data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
    data = ((os.stat(path), path) for path in data)

    # regular files, insert creation date
    data = ((stat[ST_CTIME], path)
            for stat, path in data if S_ISREG(stat[ST_MODE]))

    for cdate, path in sorted(data, reverse=True):
        pathCSV = os.path.basename(path)
        break
    session['file'] = dir_path + '/' + pathCSV
    return True   


def findFile(fecha,datos):
    # recibe tipos de datos a buscar y un rango de fechas    
    result = []     
    with open(session['file'], newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
           print(row['RecordTime'][:8])    
    return result   
# fecha de hoy para comparar        
# dt = datetime.datetime.today()
# print(str(dt.day) + '/' + str(dt.month) + '/' + str(dt.year)[:2])


