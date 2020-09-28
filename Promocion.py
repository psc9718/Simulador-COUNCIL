import pandas as pd
import numpy as np
import data as dt
import functions as ft

# -- ---------------------------------------------------------------------------------------------------- #
# Definir Variables
# Promocion
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
inversion_por_promocion = []
inversiones_porempresa = []


for j in range(0, dt.Empresas):
    for i in range(0, dt.Productos_maximos):
        lista1 = np.random.choice(np.arange(0, 10000000, 100000), size=1)
        inversion_por_promocion.append(lista1)
    inversiones_porempresa .append(inversion_por_promocion)
    inversion_por_promocion = []

# -- ---------------------------------------------------------------------------------------------------- #
# Generar aleatorios de promociones aleatorias por cada empresa y sus respectivos productos
pesos_promocion = []
pesos_promocion_porempresa = []
auxiliar = []
valor = 0

for j in range(0, dt.Empresas):
    for i in range(0, dt.Productos_maximos):
        lista1 = np.random.dirichlet(np.ones(5), size=1)
        for a in range(0, 3):
            auxiliar.append(lista1[0][a])
        pesos_promocion.append(auxiliar)
        auxiliar = []
    pesos_promocion_porempresa.append(pesos_promocion)
    pesos_promocion = []

# -- ---------------------------------------------------------------------------------------------------- #
# Realizar el indice de similitud entre los datos del usuario y los ideales

ideales = df_promocion.iloc[0]
indice_promocion = []
indice_promocion_porempresa = []

for j in range(0, dt.Empresas):
    for i in range(0, dt.Productos_maximos):
        indice = ft.euclidean_distance_conjuntos(ideales, pesos_promocion_porempresa[j][i])
        indice_promocion.append(np.exp(-indice))
    indice_promocion_porempresa.append(indice_promocion)
    indice_promocion = []
