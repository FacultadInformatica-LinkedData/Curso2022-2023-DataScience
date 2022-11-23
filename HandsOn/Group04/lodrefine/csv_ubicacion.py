import pandas as pd

df = pd.read_csv('ContenedoresOK.csv')
df['COORDX'] = df['COORDENADA-X']
df['COORDY'] = df['COORDENADA-Y']

df_ubicacion = df.copy()

def id_ubi(row):
    x = row.COORDX
    y = row.COORDY
    return f'{x}-{y}'

df_ubicacion['ID'] = df_ubicacion.apply(id_ubi, axis=1)
df['UBICACION'] = df.apply(id_ubi, axis=1)
df_ubicacion.rename(columns= {'UBICACION':'CALLE'})
df_ubicacion = df_ubicacion.reindex(columns=['ID', 'CALLE', 'DISTRITO', 'CODIGO POSTAL', 'COORDENADA-X','COORDENADA-Y'])
df = df.reindex(columns= ['ID','TIPO', 'UBICACION', 'HORARIO'])
df_ubicacion.to_csv('Ubicacion.csv')
df.to_csv('Contenedores.csv')