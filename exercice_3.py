"""Exercice 3.
"""

__authors__ = ["ZHUKOVA Nadezhda", "OUSSAREN Mohamed", "ROUAUD Lucas"]
__date__ = "31/05/2023"
__version__ = "0.0.1"
__copyright__ = "CC BY-SA"


import networkx as nx
import numpy as np
import sys

import matplotlib.pyplot as plt


def exercice_3(k, G):
    for i in range(k):
        v = input()

        cycle = nx.cycle_basis(G, v)
        cycle = [j for i in cycle for j in i]

        neigh = list(G.neighbors(v))
        dodge = __check_cycle(cycle, neigh, G, [v])

        print(dodge, flush=True)


def __check_cycle(cycle, neigh, G, list_v):
    result = 0

    for n_i in neigh:
        if n_i in list_v:
            continue

        if n_i in cycle:
            return 0
        elif len(list(G.neighbors(n_i))) == 1:
            return 1
        else:
            result += __check_cycle(
                cycle,
                list(G.neighbors(n_i)),
                G,
                list(list_v + [n_i])
            )

    return int(len(neigh) - result == 1)
