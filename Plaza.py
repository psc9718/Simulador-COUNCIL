import pandas as pd
import numpy as np
import data as dt

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
# Generar aleatorios de plazas por cada empresa y sus respectivos productos
plaza_pesos = []
pesos_plaza_porempresa = []
valor = 0

for j in range(0, dt.Empresas):
    for i in range(0, dt.Productos_maximos):
        retail = float(np.random.choice(np.arange(0, 1, .01), size=1))
        valor = 1-retail
        if valor == 0:
            lista1 = [retail, 0, 0]
            break
        telefonica = float(np.random.choice(np.arange(0, valor, .01), size=1))
        valor = 1-telefonica-retail
        if valor == 0:
            lista1 = [retail, telefonica, 0]
            break
        commerce = float(np.random.choice(np.arange(0, valor, .01), size=1))
        lista1 = [retail, telefonica, commerce]
        plaza_pesos.append(lista1)
    pesos_plaza_porempresa.append(plaza_pesos)
    plaza_pesos = []
