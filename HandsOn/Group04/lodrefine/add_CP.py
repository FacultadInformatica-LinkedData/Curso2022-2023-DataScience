import re

import pandas as pd
import utm as utm

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="madridContenedores")
df = pd.read_csv('Contenedores.csv')

df['COORDX'] = df['COORDENADA-X']
df['COORDY'] = df['COORDENADA-Y']
def coordenadas(row):
    utmx = row.COORDX
    utmy = row.COORDY
    try:
        utmx = float(utmx)
        utmy = float(utmy)
    except:

        if isinstance(utmx, str):
            utmx = utmx.replace(',', '.')
            utmx = float(utmx)

        if isinstance(utmy, str):
            utmy = utmy.replace(',', '.')
            utmy = float(utmy)

    try:
        lat, long = utm.to_latlon(utmx, utmy, 30, northern=True)
        coordenadas = f'{lat}, {long}'
    except:
        return''
    return coordenadas

def get_cp(row):
    try:
        location = geolocator.reverse(row.coordenadas)
        CP = re.findall('\d{5}', location.address)
    except:
        return ''
    if len(CP) > 0:
        return int(CP[0])
    else:
        return ''


df = df.copy()

df["coordenadas"] = df.apply(coordenadas, axis=1)
df.to_csv('con_coordenadas.csv')
print(df['coordenadas'])
df = df.copy()
df["CODIGO POSTAL"] = df.apply(get_cp, axis=1)
df = df.reindex(columns=['TIPO','ID','DIRECCION','DISTRITO','CODIGO POSTAL','COORDENADA-X', 'COORDENADA-Y', 'HORARIO'])
df.to_csv('ContenedoresOK.csv')

