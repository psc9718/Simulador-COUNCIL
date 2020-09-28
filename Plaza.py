import pandas as pd
import numpy as np
import data as dt
import functions as ft

# -- ---------------------------------------------------------------------------------------------------- #
# Definir Variables
# Plaza
Retail = list()
Retail.append(.5)
telefonica = list()
telefonica.append(.4)
e_commerce = list()
e_commerce.append(.1)

# Columnas
Plaza = ['Retail', 'Plaza', 'E-commerce']


# -- ---------------------------------------------------------------------------------------------------- #
# Plaza
# DataFrame de las características del segmento

df_Plaza = pd.DataFrame(columns=Plaza)
df_Plaza[Plaza[0]] = Retail
df_Plaza[Plaza[1]] = telefonica
df_Plaza[Plaza[2]] = e_commerce

# -- ---------------------------------------------------------------------------------------------------- #
# Generar aleatorios de inversion por producto
inversion_por_plaza = []
inversiones_porempresa = []

for j in range(0, dt.Empresas):
    for i in range(0, dt.Productos_maximos):
        lista1 = np.random.choice(np.arange(0, 10000000, 100000), size=1)
        inversion_por_plaza.append(lista1)
    inversiones_porempresa.append(inversion_por_plaza)
    inversion_por_plaza = []

# -- ---------------------------------------------------------------------------------------------------- #
# Generar aleatorios de plazas por cada empresa y sus respectivos productos
plaza_pesos = []
pesos_plaza_porempresa = []
auxiliar = []
valor = 0

for j in range(0, dt.Empresas):
    for i in range(0, dt.Productos_maximos):
        lista1 = np.random.dirichlet(np.ones(3), size=1)
        for a in range(0, 3):
            auxiliar.append(lista1[0][a])
        plaza_pesos.append(auxiliar)
        auxiliar = []
    pesos_plaza_porempresa.append(plaza_pesos)
    plaza_pesos = []

# -- ---------------------------------------------------------------------------------------------------- #
# Realizar el indice de similitud entre los datos del usuario y los ideales

ideales = df_Plaza.iloc[0]
indice_plaza = []
indice_plaza_porempresa = []

for j in range(0, dt.Empresas):
    for i in range(0, dt.Productos_maximos):
        indice = ft.euclidean_distance_conjuntos(ideales, pesos_plaza_porempresa[j][i])
        indice_plaza.append(np.exp(-indice))
    indice_plaza_porempresa.append(indice_plaza)
    indice_plaza = []