import pandas as pd
import numpy as np
import data as dt
import functions as ft
import Distribucion as dr
import scipy.spatial.distance as spsd

# -- ---------------------------------------------------------------------------------------------------- #
# Definir Variables ideales y pesos
# Plaza
Retail = list()
Retail.append(.5)
telefonica = list()
telefonica.append(.4)
e_commerce = list()
e_commerce.append(.1)

# Columnas
Plaza = ['Retail', 'Plaza', 'E-commerce']
# Definir lista de las variables ideales

# -- ---------------------------------------------------------------------------------------------------- #
# Plaza
# DataFrame de las características del segmento

df_Plaza = pd.DataFrame(columns=Plaza)
df_Plaza[Plaza[0]] = Retail
df_Plaza[Plaza[1]] = telefonica
df_Plaza[Plaza[2]] = e_commerce

# -- ---------------------------------------------------------------------------------------------------- #
# Generar aleatorios de la seleccion de inversion para cada uno de los productos que tienen las empresas
inversion_por_plaza = ft.get_inversiones(dt.Empresas, dt.Productos_maximos)

# -- ---------------------------------------------------------------------------------------------------- #
# Generar aleatorios de plazas por cada empresa y sus respectivos productos
# Generar decisiones que toma cada empresa para los pesos de las plazas.
pesos_plaza_porempresa = ft.get_aleatorios(dt.Empresas, dt.Productos_maximos, 3)

# -- ---------------------------------------------------------------------------------------------------- #
# Realizar el indice de similitud entre los datos del usuario y los ideales
# calcular similitud que tiene los pesos de decision de cada empresa con los ideales del mercado.
similitud_plaza = ft.get_similitud(dt.Empresas, dt.Productos_maximos, df_Plaza.iloc[0], pesos_plaza_porempresa)

# -- ---------------------------------------------------------------------------------------------------- #
# Realizar el indice de similitud entre los datos la inversión ideal
# Similitud de los ideales del mercado contra las decisiones de la empresa

similitud_inversion = []
auxiliar = []

for i in range(0, dt.Empresas):
    for j in range(0, dt.Productos_maximos):
        indice = spsd.euclidean(float(inversion_por_plaza[i][j]), dt.inversion_ideal)
        indice = np.exp(-indice)
        auxiliar.append(indice)
    similitud_inversion.append(auxiliar)
    auxiliar = []

# -- ---------------------------------------------------------------------------------------------------- #
# Similitud total de promocion
# Calcular un promedio ponderado de las dos similitudes para ver cual es la similitud total.

peso_inversion = .5
peso_pesos = .5
auxiliar = []
similitud_plaza_total = []

for i in range(0, dt.Empresas):
    for j in range(0, dt.Productos_maximos):
        indice = similitud_inversion[i][j]*peso_inversion+peso_pesos*similitud_plaza[i][j]
        auxiliar.append(indice)
    similitud_plaza_total.append(auxiliar)
    auxiliar = []

# -- ---------------------------------------------------------------------------------------------------- #
# Posicionamiento
# El posicionamiento tiene que ver con las decisiones de distribucion y plaza

posicionamiento = []
auxiliar = []
peso_dr = .5
peso_pl = .5

for i in range(0, dt.Empresas):
    for j in range(0, dt.Productos_maximos):
        indice = dr.similitud_distribucion[i][j] * peso_dr + peso_pl * similitud_plaza_total[i][j]
        auxiliar.append(indice)
    posicionamiento.append(auxiliar)
    auxiliar = []
