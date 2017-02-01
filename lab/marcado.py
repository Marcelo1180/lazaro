import csv
from datetime import datetime

def conv_time(ix_data):
    return datetime.strptime(ix_data, '%H:%M:%S')


def control_intervalo(ix_data, ix_intervalo, ix_cont):
    x_data = conv_time(ix_data)
    for indx, row in ix_intervalo.iteritems():
        # print
        if conv_time(row["min_entrada"]) <= x_data and x_data <= conv_time(row["entrada"]):
            ix_cont = 1
            print "verde"

        if conv_time(row["entrada"]) < x_data and x_data < conv_time(row["salida"]):
            print "amarillo %s" % ix_cont
            ix_cont+=1

        if conv_time(row["salida"]) <= x_data and x_data <= conv_time(row["max_salida"]):
            print "rojo"

    return ix_cont


def control_asistencia(ix_data, ix_intervalo, ix_usuario, ix_fecha):
    cont = 0
    for row in ix_data:
        if row[2] == ix_usuario and row[3] == ix_fecha:
            cont += 1
            print datetime.strptime(row[4], '%H:%M:%S')


    return cont


conf_intervalo={
    "manana":{
        "min_entrada":"05:00:00",
        "entrada":"08:40:00",
        "salida":"12:00:00",
        "max_salida":"14:00:00",
    }
}
cont_marcado=0

ifile  = open('asistencia.csv', "rb")
reader = csv.reader(ifile)

# control_intervalo("08:34:25", conf_intervalo)
# control_intervalo("08:40:00", conf_intervalo)
arr_hr = ["08:40:01", "10:40:01", "12:40:15"]

cont = 1
for arr_i in arr_hr:
    cont = control_intervalo(arr_i, conf_intervalo, cont)
    print "permiso de %s a %s" % (arr_i[])

# control_asistencia(reader, conf_intervalo, "jarteaga", "2017-01-03")

ifile.close()
