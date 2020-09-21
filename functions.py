import numpy as np

# -- ---------------------------------------------------------------------------------------------------- #
# Definir cantidad de empresas y productos maximos

Empresas = 6
Productos_maximos = 8
total = 6*8

# -- ---------------------------------------------------------------------------------------------------- #
# Generar aleatorios de caracteristicas

caracteristicas_productos_porempresa = []
productos_porempresas = []

for j in range(0, Empresas):
    for i in range(0, Productos_maximos):
        productos_porempresas.append(([float(np.random.choice(np.arange(5.1, 6.9, .01), size=1)),
                                       float(np.random.randint(7, 13, 1)),
                                       float(np.random.choice(np.arange(3000, 4000, 100), size=1)),
                                       float(np.random.randint(5, 7, 1)), float(np.random.randint(7000, 9000, 1))]))
    caracteristicas_productos_porempresa.append(productos_porempresas)
    productos_porempresas = []
