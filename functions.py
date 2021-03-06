import numpy as np
from scipy.spatial import distance

# -- ---------------------------------------------------------------------------------------------------- #
# Funciones para indices de similitud


def jaccard(list1, list2):
    # Funcion que calcula la similitud de jaccard, recordar que la restriccion es que es para numeros binarios
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union


def euclidean_distance_conjuntos(x, y):
    # Calcula similitud euclidiana entre dos listas
    return np.sqrt(sum(pow(a-b, 2) for a, b in zip(x, y)))


def euclidean_distance_elementos(x, y):
    # Calcula similitud euclidiana entre dos valores
    return np.exp(-np.sqrt(pow(x-y, 2)))

# -- ---------------------------------------------------------------------------------------------------- #
# Generacion de numeros aleatorios entre 0 y 1


def get_aleatorios(empresas, productos, cantidad):
    # Funcion que retorna aleatorios entre 0 y 1 para otorgar los porcentajes.
    aleatorios_individuales = []
    aleatorios_empresa = []
    auxiliar = []

    for j in range(0, empresas):
        for i in range(0, productos):
            lista1 = np.random.dirichlet(np.ones(cantidad), size=1)
            for a in range(0, cantidad):
                auxiliar.append(lista1[0][a])
            aleatorios_individuales.append(auxiliar)
            auxiliar = []
        aleatorios_empresa.append(aleatorios_individuales)
        aleatorios_individuales = []

    return aleatorios_empresa

# -- ---------------------------------------------------------------------------------------------------- #
# Funcion que genera aleatorios de inversion entre 0 a 10000000


def get_inversiones(empresas, productos):
    # Funcion que retorna la decision de cada empresa para cada producto de inversion. Escala del 0 al 100.
    inversion_individual = []
    inversiones_porempresa = []

    for j in range(0, empresas):
        for i in range(0, productos):
            lista1 = np.random.choice(np.arange(0, 100, 1), size=1)
            inversion_individual.append(lista1)
        inversiones_porempresa.append(inversion_individual)
        inversion_individual = []

    return inversiones_porempresa

# -- ---------------------------------------------------------------------------------------------------- #
# Funcion que realiza el indice de similitud para las listas de este proyecto


def get_pesos(cantidad, empresas, productos, variables, pesos):
    # Funcion que calcula los los ideales por su peso.
    for j in range(0, empresas):
        for k in range(0, productos):
            for i in range(0, cantidad):
                variables[j][k][i] = variables[j][k][i]*pesos[i]
    return variables

# -- ---------------------------------------------------------------------------------------------------- #
# Funcion que realiza el indice de similitud para las listas de este proyecto


def get_similitud(empresas, productos, ideales, lista_comparar):
    # Funcion que calcula la similitud entre dos listas que le mandes, utilizando la librería de scipy.
    indice_individual = []
    indice_porempresas = []
    for j in range(0, empresas):
        for i in range(0, productos):
            indice = distance.euclidean(ideales, lista_comparar[j][i])
            indice_individual.append(np.exp(-indice))
        indice_porempresas.append(indice_individual)
        indice_individual = []

    return indice_porempresas
