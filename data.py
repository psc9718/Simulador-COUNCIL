
import pandas as pd

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

# Plaza
Retail = list()
Retail.append(.5)
telefonica = list()
telefonica.append(.4)
e_commerce = list()
e_commerce.append(.1)

# Columnas
caracteristicas = ['Pantalla', 'Camara', 'Bateria', 'Procesador', 'Precio']
promocion = ['Redes Sociales', 'Television', 'Bateria', 'Procesador', 'Precio']
Plaza = ['Retail', 'Plaza', 'E-commerce']

# -- ---------------------------------------------------------------------------------------------------- #
# Area Investigacion y Desarrollo
# DataFrame de las características del segmento

df_caracteristicas = pd.DataFrame(columns=caracteristicas)
df_caracteristicas[caracteristicas[0]] = Pantalla
df_caracteristicas[caracteristicas[1]] = Camara
df_caracteristicas[caracteristicas[2]] = Bateria
df_caracteristicas[caracteristicas[3]] = Procesador
df_caracteristicas[caracteristicas[4]] = Precio

df_caracteristicas_pesos = pd.DataFrame(columns=caracteristicas)
df_caracteristicas_pesos[caracteristicas[0]] = p_pantalla
df_caracteristicas_pesos[caracteristicas[1]] = p_camara
df_caracteristicas_pesos[caracteristicas[2]] = p_bateria
df_caracteristicas_pesos[caracteristicas[3]] = p_procesador
df_caracteristicas_pesos[caracteristicas[4]] = p_precio
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
# Promocion
# DataFrame de las características del segmento

df_Plaza = pd.DataFrame(columns=Plaza)
df_Plaza[Plaza[0]] = Retail
df_Plaza[Plaza[1]] = telefonica
df_Plaza[Plaza[2]] = e_commerce

