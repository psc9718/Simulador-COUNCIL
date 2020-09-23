import pandas as pd
import numpy as np
import data as dt

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
# Generar aleatorios de promociones aleatorias por cada empresa y sus respectivos productos
pesos_promocion = []
pesos_promocion_porempresa = []
valor = 0

for j in range(0, dt.Empresas):
    for i in range(0, dt.Productos_maximos):
        redes_sociales = float(np.random.choice(np.arange(0, 1, .01), size=1))
        valor = 1-redes_sociales
        if valor == 0:
            lista1 = [redes_sociales, 0, 0, 0, 0]
            break
        television = float(np.random.choice(np.arange(0, valor, .01), size=1))
        valor = 1-television-redes_sociales
        if valor == 0:
            lista1 = [redes_sociales, television, 0, 0, 0]
            break
        mkt_directo = float(np.random.choice(np.arange(0, valor, .01), size=1))
        valor = 1-television-redes_sociales-mkt_directo
        if valor == 0:
            lista1 = [redes_sociales, television, mkt_directo, 0, 0]
            break
        Radio = float(np.random.choice(np.arange(0, valor, .01), size=1))
        valor = 1 - television - redes_sociales - mkt_directo - Radio
        if valor == 0:
            lista1 = [redes_sociales, television, mkt_directo, Radio, 0]
            break
        impresos = float(np.random.choice(np.arange(0, valor, .01), size=1))
        lista1 = [redes_sociales, television, mkt_directo, Radio, impresos]
        pesos_promocion.append(lista1)
    pesos_promocion_porempresa.append(pesos_promocion)
    pesos_promocion = []
