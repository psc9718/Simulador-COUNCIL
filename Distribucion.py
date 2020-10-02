import Plaza as pl
import data as dt
import numpy as np
import functions as ft

# -- ---------------------------------------------------------------------------------------------------- #
# Importar los datos necesarios

ideales = pl.df_Plaza.iloc[0]

# -- ---------------------------------------------------------------------------------------------------- #
# Generar aleatorios de plazas por cada empresa y sus respectivos productos
pesos_distribucion_porempresa = ft.get_aleatorios(dt.Empresas, dt.Productos_maximos, 3)

# -- ---------------------------------------------------------------------------------------------------- #
# Realizar el indice de similitud entre los datos del usuario y los ideales

similitud_distribucion = ft.get_similitud(dt.Empresas, dt.Productos_maximos, ideales, pesos_distribucion_porempresa)
