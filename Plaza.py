import pandas as pd

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
