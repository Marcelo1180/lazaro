import pandas as pd
from datetime import datetime

def conv_time(ix_data):
    return datetime.strptime(ix_data, '%H:%M:%S')

def unconv_time(ix_data):
    return ix_data.strftime('%H:%M:%S')

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

import csv
ifile  = open('asistencia.csv', "rb")
reader = csv.reader(ifile)

# arr_hr = ["08:40:01", "10:40:01", "12:40:15"]
# arr_hr = ["08:42:01","09:00:00","10:30:00","11:00:00","11:30:00","12:40:15"]
# arr_hr = ["08:30:12", "08:40:01", "10:40:01", "12:40:15"]
arr_hr = ["08:30:01", "10:40:01"]

asistencia_base={
    "entrada" :"",
    "permisos":[],
    "salida"  :"",
}


# df = pd.Series(arr_hr)
# di = pd.to_datetime()
# df.between_time(start_time="05:00", end_time="08:40")
import pandas as pd
C = pd.Series(arr_hr)

# df = pd.DataFrame()
# df['C'] = C
# df['ax'] = 'A'
df = pd.read_csv('asistencia.csv', parse_dates=["Hora"])
df["key_hora"] = df["Hora"]
# print df
# df['Hora'] = pd.DatetimeIndex(df['Hora'])

# parse_dates = ['Hora']
#set index to the obervations after converting them to type datetimeIndex
# df.index = ["Hora"]
df.set_index(keys=["key_hora"], inplace=True)
# df.columns = ["Hora", "Nombre"]
# print df


intx = df.between_time(start_time="05:00:00", end_time="08:40:00")
print intx.groupby(["Fecha", "Nombre"]).min()

# inty = df.between_time(start_time="08:40:00", end_time="12:00:00")
# inty2 = inty.groupby(["Fecha", "Nombre", "Hora"])
# # inty2['counter'] = range(len(inty2))
# print inty2

# intx = df.between_time(start_time="05:00:00", end_time="08:40:00")
# print intx.groupby(["Fecha", "Nombre"]).min()



# print intx

# print intx
# print intx.groupby(["Fecha", "Nombre"], sort=False)
# print max(intx.idxmax())


# print df.between_time(df['C'][0],df['C'][2])

# index = pd.date_range(start='2012-11-05 01:00:00', end='2012-11-05 23:00:00', freq='15').tz_localize('UTC')
# df=pd.DataFrame(range(len(index)), index=index, columns=['Number'])
