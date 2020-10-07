import pandas as pd
import numpy as np
import data as dt
import functions as ft
import scipy.spatial.distance as spsd

# -- ---------------------------------------------------------------------------------------------------- #
# Definir Variables ideales y pesos
# Promocions
Redes_sociales = list()
Redes_sociales.append(.5)
Television = list()
Television.append(.25)
mkt_directo = list()
mkt_directo.append(.15)
Radio = list()
Radio.append(.05)
impresos = list()
impresos.append(.05)
inversion_ideal = 6500000

# Columnas
promocion = ['Redes Sociales', 'Television', 'Bateria', 'Procesador', 'Precio']


# -- ---------------------------------------------------------------------------------------------------- #
# Promocion
# DataFrame de las características del segmento

df_promocion = pd.DataFrame(columns=promocion)
df_promocion[promocion[0]] = Redes_sociales
df_promocion[promocion[1]] = Television
df_promocion[promocion[2]] = mkt_directo
df_promocion[promocion[3]] = Radio
df_promocion[promocion[4]] = impresos

# -- ---------------------------------------------------------------------------------------------------- #
# Generar aleatorios de inversion por producto

inversion_por_promocion = ft.get_inversiones(dt.Empresas, dt.Productos_maximos)
# -- ---------------------------------------------------------------------------------------------------- #
# Generar aleatorios de promociones aleatorias por cada empresa y sus respectivos productos

pesos_promocion_porempresa = ft.get_aleatorios(dt.Empresas, dt.Productos_maximos, 5)
# -- ---------------------------------------------------------------------------------------------------- #
# Realizar el indice de similitud entre los datos del usuario y los ideales

similitud_promocion = ft.get_similitud(dt.Empresas, dt.Productos_maximos, df_promocion.iloc[0],
                                       pesos_promocion_porempresa)

# -- ---------------------------------------------------------------------------------------------------- #
# Realizar el indice de similitud entre los datos la inversión ideal

similitud_inversion = []
auxiliar = []

for i in range(0, dt.Empresas):
    for j in range(0, dt.Productos_maximos):
        indice = spsd.euclidean(float(inversion_por_promocion[i][j]), dt.inversion_ideal)
        indice = np.exp(-indice)
        auxiliar.append(indice)
    similitud_inversion.append(auxiliar)
    auxiliar = []

# -- ---------------------------------------------------------------------------------------------------- #
# Similitud total de promocion

peso_inversion = .5
peso_pesos = .5
auxiliar = []
similitud_promocion_total = []

for i in range(0, dt.Empresas):
    for j in range(0, dt.Productos_maximos):
        indice = similitud_inversion[i][j]*peso_inversion+peso_pesos*similitud_promocion[i][j]
        auxiliar.append(indice)
    similitud_promocion_total.append(auxiliar)
    auxiliar = []

# -- ---------------------------------------------------------------------------------------------------- #
# Accesibilidad de cada uno de los productos

Accesibilidad = similitud_promocion

