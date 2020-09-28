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
inversion_por_plaza = ft.get_inversiones(dt.Empresas, dt.Productos_maximos)

# -- ---------------------------------------------------------------------------------------------------- #
# Generar aleatorios de plazas por cada empresa y sus respectivos productos
pesos_plaza_porempresa = ft.get_aleatorios(dt.Empresas, dt.Productos_maximos, 3)

# -- ---------------------------------------------------------------------------------------------------- #
# Realizar el indice de similitud entre los datos del usuario y los ideales
pesos = [np.ones(3)]
similitud_plaza = ft.get_similitud(dt.Empresas, dt.Productos_maximos, df_Plaza.iloc[0], pesos_plaza_porempresa, pesos)
