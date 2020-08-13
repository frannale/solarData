import csv
from flask import session,request
import datetime
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time
import datetime as dt

def getFile():
    # traigo datos del csv mas reciente
    dir_path = os.getcwd() + '/CSVFiles'
    data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
    data = ((os.stat(path), path) for path in data)

    # regular files, insert creation date
    data = ((stat[ST_CTIME], path)
            for stat, path in data if S_ISREG(stat[ST_MODE]))

    for cdate, path in sorted(data, reverse=True):
        print(path)
        pathCSV = os.path.basename(path)
        break
    session['file'] = dir_path + '/' + pathCSV
    return True   


def findFile(fecha,datos):
    # recibe tipos de datos a buscar y un rango de fechas    
    result = {}
    dir_path = os.getcwd() + '/CSVFiles'
    data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
    data = ((os.stat(path), path) for path in data)

    # regular files, insert creation date
    data = ((stat[ST_CTIME], path)
            for stat, path in data if S_ISREG(stat[ST_MODE]))

    for cdate, path in sorted(data, reverse=True):
        print(path)
        pathCSV = os.path.basename(path)
        break
    # CREO ESTRUCTURA CONTENEDORA DE DATOS
    dias = []
    for x in range(int(fecha)):
        fechaHoy = dt.date.today() - dt.timedelta(days=x)
        result[fechaHoy.strftime("%d/%m/%y").strip()]= {}
        dias.append(fechaHoy.strftime("%d/%m/%y").strip())
        for x in datos:
            result[fechaHoy.strftime("%d/%m/%y").strip()][x]= []
    result['06/03/20']= {}
    for x in datos:
            result['06/03/20'][x]= []
    dias.append('06/03/20')
    print(result) 
    with open(dir_path + '/' + pathCSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            fechaRow = row['RecordTime'][0:8].replace("\n", "")
            print(11) 
            if( fechaRow in dias):
                print(11)
                for x in datos:
                    result[fechaHoy.strftime("%d/%m/%y").strip()][x].append(row[x])
                break
    print(result)          
    return result   


findFile(1,['Grid voltage','RecordTime'])