import Plaza as pl
import data as dt
import functions as ft

# -- ---------------------------------------------------------------------------------------------------- #
# Importar los datos necesarios

ideales = pl.df_Plaza.iloc[0]  # Importar los pesos de Plaza ya que estos son los mismos para distribución.


# -- ---------------------------------------------------------------------------------------------------- #
# Generar aleatorios de plazas por cada empresa y sus respectivos productos

# Generar las decisiones de pesos que toma cada empresa para cada uno de sus productos.
pesos_distribucion_porempresa = ft.get_aleatorios(dt.Empresas, dt.Productos_maximos, 3)

# -- ---------------------------------------------------------------------------------------------------- #
# Realizar el indice de similitud entre los datos del usuario y los ideales

# Sacar las similitud que existe entre los ideales del mercado de plaza y los datos elegidos por cada una de las
# empresas
similitud_distribucion = ft.get_similitud(dt.Empresas, dt.Productos_maximos, ideales, pesos_distribucion_porempresa)
