import numpy as np
# -- ---------------------------------------------------------------------------------------------------- #
# Funcion que calcula el indice de similtud de jaccard entre dos listas


def jaccard(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union


def euclidean_distance_conjuntos(x, y):
    return np.sqrt(sum(pow(a-b, 2) for a, b in zip(x, y)))


def euclidean_distance_elementos(x, y):
    return np.exp(-np.sqrt(pow(x-y, 2)))
