
import csv
import datetime
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time
import datetime as dt


def pre_process():
    # columnas que se mantienen
    print(getFile)
    keep_col = ['AccumulatedDischargerPower','AccumulatedLoadPower','AccumulatedSelfusePower','AccumulatedPvPower']
    data_anterior = {'AccumulatedDischargerPower' : 0,'AccumulatedLoadPower' : 0,'AccumulatedSelfusePower' : 0,'AccumulatedPvPower' : 0}
    meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril',5:'mayo', 6:'junio', 7:'julio', 8:'agosto',9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
    # ABRIMOS LOS DOS CSV
    with open(getFile(), 'r') as read_obj, open(getFile().replace('.csv','_PROCESADO.csv'), 'w') as write_obj:
        csv_reader = csv.DictReader(read_obj)
        csv_writer = csv.writer(write_obj)
        # CREO LOS HEADERS
        new_row = []
        for i in keep_col:
            new_row.append(i)
        new_row.append('Hora')
        new_row.append('Dia')    
        new_row.append('Mes')
        new_row.append('Anio')
        # INSERTO HEADERS
        csv_writer.writerow(new_row)
        # RECORRO LAS ROWS
        for row in csv_reader:
            new_row =  []          
            for nombre_columna in keep_col:
                # VERIFICACION POR CADA ACUMULATED PARA HACER EL CALCULO
                if( "Accumulated" in nombre_columna ):
                    difference = float(row[nombre_columna].replace('KWH','')) - data_anterior[nombre_columna]
                    new_row.append(row[nombre_columna] + ' (+ '  + str(difference) + ' KWH) ' ) 
                    data_anterior[nombre_columna] = float(row[nombre_columna].replace('KWH',''))
                else:               
                    new_row.append(row[i])
            # DATE FORMAT = 29/01/2020 11:06:31 p.m.        
            new_row.append(row['RecordTime'][11:23])
            new_row.append(row['RecordTime'][0:2])          
            new_row.append(meses[int(row['RecordTime'][3:5])]) 
            new_row.append(row['RecordTime'][6:10]) 
            # Add the updated row
            csv_writer.writerow(new_row)
          
    return True 

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
    return dir_path + '/' + pathCSV  

print(pre_process())

