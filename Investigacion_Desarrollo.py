import pandas as pd
import data as dt
import numpy as np
import functions as ft

# -- ---------------------------------------------------------------------------------------------------- #
# Definir Variables

# Investigacion y Desarrollo
Precio = list()
Precio.append(7999)
p_precio = list()
p_precio.append(.5)
Pantalla = list()
Pantalla.append(6.0)
p_pantalla = list()
p_pantalla.append(.25)
Camara = list()
Camara.append(10)
p_camara = list()
p_camara.append(.15)
Bateria = list()
Bateria.append(3500)
p_bateria = list()
p_bateria.append(.05)
Procesador = list()
Procesador.append(6.0)
p_procesador = list()
p_procesador.append(.05)

# Columnas
caracteristicas = ['Pantalla', 'Camara', 'Bateria', 'Procesador', 'Precio']

# -- ---------------------------------------------------------------------------------------------------- #
# Area Investigacion y Desarrollo
# DataFrame de las características del segmento


def get_df(v1, v2, v3, v4, v5):
    df = pd.DataFrame(columns=caracteristicas)
    df[caracteristicas[0]] = v1
    df[caracteristicas[1]] = v2
    df[caracteristicas[2]] = v3
    df[caracteristicas[3]] = v4
    df[caracteristicas[4]] = v5
    return df


df_caracteristicas = get_df(Pantalla, Camara, Bateria, Procesador, Precio)
df_carac_pesos = get_df(p_pantalla, p_camara, p_bateria, p_procesador, p_precio)

# -- ---------------------------------------------------------------------------------------------------- #
# Generar aleatorios de caracteristicas

caracteristicas_productos_porempresa = []
productos_porempresas = []

for j in range(0, dt.Empresas):
    for i in range(0, dt.Productos_maximos):
        Pantalla = float(np.random.choice(np.arange(5.1, 6.9, .01), size=1))
        Camara = float(np.random.randint(7, 13, 1))
        Bateria = float(np.random.choice(np.arange(3000, 4000, 100), size=1))
        Procesador = float(np.random.randint(5, 7, 1))
        Precio = float(np.random.randint(7000, 9000, 1))
        lista1 = [Pantalla, Camara, Bateria, Procesador, Precio]
        productos_porempresas.append(lista1)
    caracteristicas_productos_porempresa.append(productos_porempresas)
    productos_porempresas = []

# -- ---------------------------------------------------------------------------------------------------- #
# Realizar el indice de similitud entre los datos del usuario y los ideales

ideales = df_caracteristicas.iloc[0] #*df_carac_pesos.iloc[0]
indice_caracteristicas = []
indice_productos_porempresa = []

for j in range(0, dt.Empresas):
    for i in range(0, dt.Productos_maximos):
        indice = ft.euclidean_distance_conjuntos(ideales,
                                                 caracteristicas_productos_porempresa[j][i])#*df_carac_pesos.iloc[0])
        indice_caracteristicas.append(np.exp(-indice))
    indice_productos_porempresa.append(indice_caracteristicas)
    indice_caracteristicas = []
