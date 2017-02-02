import csv
from datetime import datetime

def conv_time(ix_data):
    return datetime.strptime(ix_data, '%H:%M:%S')

def unconv_time(ix_data):
    return ix_data.strftime('%H:%M:%S')

def control_intervalo(ix_data, ix_intervalo, ix_asistencia):
    x_data = conv_time(ix_data)
    for indx, row in ix_intervalo.iteritems():
        # print
        if conv_time(row["min_entrada"]) <= x_data and x_data <= conv_time(row["entrada"]):
            ix_asistencia[indx]["entrada"]=unconv_time(x_data)
            print row, indx
            # print "verde"

        if conv_time(row["entrada"]) < x_data and x_data < conv_time(row["salida"]):
            if not ix_asistencia[indx]["entrada"] and not ix_asistencia[indx]["permisos"]:
                ix_asistencia[indx]["permisos"].append("-")
            ix_asistencia[indx]["permisos"].append(unconv_time(x_data))

            # print "amarillo"

        if conv_time(row["salida"]) <= x_data and x_data <= conv_time(row["max_salida"]):
            # print "rojo"
            ix_asistencia[indx]["salida"]=unconv_time(x_data)
            # ix_permisos.append("x_data")
        import ipdb; ipdb.set_trace()

    # if not ix_asistencia[indx]["salida"]:
        # ix_asistencia[indx]["permisos"].append("-")


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
    },
    "tarde":{
        "min_entrada":"14:00:01",
        "entrada":"14:30:00",
        "salida":"19:00:00",
        "max_salida":"11:59:59",
    }
}
cont_marcado=0

ifile  = open('asistencia.csv', "rb")
reader = csv.reader(ifile)

# control_intervalo("08:34:25", conf_intervalo)
# control_intervalo("08:40:00", conf_intervalo)
# arr_hr = ["08:40:01", "10:40:01", "12:40:15"]
# arr_hr = ["08:42:01","09:00:00","10:30:00","11:00:00","11:30:00","12:40:15"]
# arr_hr = ["08:30:12", "08:40:01", "10:40:01", "12:40:15"]
arr_hr = ["08:30:01", "10:40:01"]

# cont = 1
asistencia_base={
    "entrada" :"",
    "permisos":[],
    "salida"  :"",
}

indice=[xind for xind, xrow in conf_intervalo.iteritems()]
# asistencia = dict(zip(indice, [asistencia_base]*len(indice)))
asistencia = dict(zip(["manana","tarde"], [asistencia_base]*len(indice)))

for a_val in arr_hr:
    control_intervalo(a_val, conf_intervalo, asistencia)

# for xind, xrow in conf_intervalo.iteritems():
#     if not asistencia[xind]["salida"]:
#         asistencia[xind]["permisos"].append("-")

    # print "permiso de %s a %s" % (a_ind, a_val)
# print asistencia
import json
print json.dumps(asistencia, indent=4, sort_keys=True)
# control_asistencia(reader, conf_intervalo, "jarteaga", "2017-01-03")

ifile.close()
