import Plaza as pl
import Promocion as pr
import Distribucion as dr
import Investigacion_Desarrollo as ide
import data as dt
import numpy as np
import pandas as pd

# -- ---------------------------------------------------------------------------------------------------- #
# Calcular similitudes totales por producto

peso_pl = .25
peso_pr = .25
peso_dr = .25
pesos_ide = .25
auxiliar = []
similitud_xprod_total = []

for i in range(0, dt.Empresas):
    for j in range(0, dt.Productos_maximos):
        valor = peso_pl * float(pl.similitud_plaza_total[i][j]) + peso_pr * float(pr.similitud_promocion_total[i][j]) +\
                peso_dr * float(dr.similitud_distribucion[i][j]) + pesos_ide * float(ide.similitud_productos[i][j])
        auxiliar.append(valor)
    similitud_xprod_total.append(auxiliar)
    auxiliar = []

# -- ---------------------------------------------------------------------------------------------------- #
# Calcular cuánto alcanzó del mercado cada uno de los productos en procentaje

suma = np.sum(similitud_xprod_total)
auxiliar = []
porcentaje_producto_mercado = []

for i in range(0, dt.Empresas):
    for j in range(0, dt.Productos_maximos):
        producto = similitud_xprod_total[i][j]
        valor = producto/suma
        auxiliar.append(valor)
    porcentaje_producto_mercado.append(auxiliar)
    auxiliar = []

# -- ---------------------------------------------------------------------------------------------------- #
# Calcular cuánto alcanzó del mercado cada uno de los productos en cantidad de productos
# ¿Cuántos productos se vendieron por cada uno de los productos que había?

auxiliar = []
cantidad_producto_mercado = []

for i in range(0, dt.Empresas):
    for j in range(0, dt.Productos_maximos):
        producto = porcentaje_producto_mercado[i][j]
        valor = round(producto*dt.tamano_del_mercado)
        auxiliar.append(valor)
    cantidad_producto_mercado.append(auxiliar)
    auxiliar = []

# -- ---------------------------------------------------------------------------------------------------- #
# Calcular cuánto alcanzó del mercado cada uno de los productos en cantidad de productos
# ¿Cuántos productos se vendieron por cada empresa?

cantidad_porempresa = []

for i in range(0, dt.Empresas):
    valor = np.sum(cantidad_producto_mercado[i])
    cantidad_porempresa.append(valor)

cantidad_maxima_empresa = np.max(cantidad_porempresa)
posicion_empresa = cantidad_porempresa.index(max(cantidad_porempresa))
print('La empresa que más vendió fue la empresa', posicion_empresa+1, 'con un total de', cantidad_maxima_empresa)

# -- ---------------------------------------------------------------------------------------------------- #
# Calcular máximos de cada empresa y la posición de ese máximo

maximos = []
posiciones = []
empresas = [1, 2, 3, 4, 5, 6]

for i in cantidad_producto_mercado:
    maximos.append(max(i))
    posiciones.append(i.index(max(i)))

df_maximos = pd.DataFrame(columns=['Empresa', 'Producto', 'Maximo'])
df_maximos['Empresa'] = empresas
df_maximos['Producto'] = posiciones
df_maximos['Maximo'] = maximos
df_maximos.index = df_maximos['Empresa']
del df_maximos["Empresa"]

maximo = 0
posicion = 0
for i in range(0, dt.Empresas):
    if maximos[i] > maximo:
        maximo = maximos[i]
        posicion = posiciones[i]

empresa_prod_max = int(np.where(maximo==df_maximos['Maximo'])[0])

print('El producto que más vendió es el producto', posicion+1, 'de la empresa', empresa_prod_max+1, 'con', maximo,
      'productos vendidos')
