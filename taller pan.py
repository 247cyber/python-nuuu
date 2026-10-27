import pandas as pd

df=pd.read_excel("pruebas de python.xlsx")
mayores_25 = df[df['edad'] > 25]
ciudades_bogota= df[df['ciudad'] == 'bogota']
edades_24 = df.loc[df["edad"] == 24, "edad"]
print(mayores_25)
print(ciudades_bogota)
print(edades_24)