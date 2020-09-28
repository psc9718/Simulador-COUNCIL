import Plaza as pl
import data as dt
import numpy as np
import functions as ft

# -- ---------------------------------------------------------------------------------------------------- #
# Importar los datos necesarios

ideales = pl.df_Plaza

# -- ---------------------------------------------------------------------------------------------------- #
# Generar aleatorios de plazas por cada empresa y sus respectivos productos
distribucion_pesos = []
pesos_distribucion_porempresa = []
auxiliar = []
valor = 0

for j in range(0, dt.Empresas):
    for i in range(0, dt.Productos_maximos):
        lista1 = np.random.dirichlet(np.ones(3), size=1)
        for a in range(0, 3):
            auxiliar.append(lista1[0][a])
        distribucion_pesos.append(auxiliar)
        auxiliar = []
    pesos_distribucion_porempresa.append(distribucion_pesos)
    plaza_pesos = []

# -- ---------------------------------------------------------------------------------------------------- #
# Realizar el indice de similitud entre los datos del usuario y los ideales

ideales = ideales.iloc[0]
indice_distribucion = []
indice_distribucion_porempresa = []

for j in range(0, dt.Empresas):
    for i in range(0, dt.Productos_maximos):
        indice = ft.euclidean_distance_conjuntos(ideales, pesos_distribucion_porempresa[j][i])
        indice_distribucion.append(np.exp(-indice))
    indice_distribucion_porempresa.append(indice_distribucion)
    indice_plaza = []
