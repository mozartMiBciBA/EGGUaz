
#08-08-19
"""
En esta ocasión te tenemos un vídeo, donde:
🔖Hacemos las operaciones con un dataframe, para obtener las 5 sumatorias
🔖Calculamos b0 y b1
🔖Comparamos los resultados utilizando StatsModels
Esperamos que este vídeo te sea de utilidad, no olvides dejarnos tus comentarios y sugerencias, nos dará mucho gusto saludarte.
📥 Descarga los archivos que salieron en el vídeo
https://drive.google.com/open?id=1nxu...

"""

import pandas as pd
df=pd.read_csv('reg.csv')

#Con esta instrucción no se nececita recorrer la columna con un ciclo for

sumax=df['x'].sum()
sumay=df['y'].sum()

#Crear una columna nueva
#Elevar al cuadrado a cada uno de los elementos de la columna x
df['x2']=df['x'].apply(lambda x: pow(x,2))
#Crear una columna nueva
#Elevar al cuadrado a cada uno de los elementos de la columna y
df['y2']=df['y'].apply(lambda x: pow(x,2))

#hacer las sumas de x2 y y2 (y al cuadrado)
sumax2=df['x2'].sum()
sumay2=df['y2'].sum()
df['xy']= df['x']*df['y']
sumaxy=df['xy'].sum()
print("Numero de datos")
n=len(df['x'])
print(n)

#yprom=sumay/n
#print(" y Promedio metodo1")
#print(yprom)

#otra forma de obtener el promedio es
print(" y Promedio metodo2")
print(df['y'].mean())
yprom=(df['y'].mean())
xprom=(df['x'].mean())

#La formula para b1 y b0

b1=(sumaxy-(1/n)*(sumax*sumay))/((sumax2)-(1/n)*pow(sumax,2))
b0=yprom-b1*xprom
print("b1",b1)
print("b0",b0)

#otra forma es con stats models.
import statsmodels.formula.api as smf
#ols = ordinari list squares= minimos cuadrados
#representa los modelos que se van a ajustar por este metodo
reg=smf.ols('y~x',data=df)
res=reg.fit()
print("Parametros")
print(res.params)


