"""Exercice 3.
"""

__authors__ = ["ZHUKOVA Nadezhda", "OUSSAREN Mohamed", "ROUAUD Lucas"]
__date__ = "31/05/2023"
__version__ = "0.0.1"
__copyright__ = "CC BY-SA"


import networkx as nx
import sys


def exercice_3(k, G):
    for i in range(k):
        v = input()

        cycle = nx.cycle_basis(G, v)
        cycle = [j for i in cycle for j in i]

        neigh = list(G.neighbors(v))
        
        # if v in cycle:
        #     dodge = 0
        # elif len(list(G.neighbors(v))) == 1:
        #     dodge = 1
        # else:
        dodge = __check_cycle(cycle, neigh, G, [v], v)

        print(dodge, flush=True)


def __check_cycle(cycle, neigh, G, list_v, act_v):
    result = 0

    if act_v in cycle:
        return 0
    elif len(list(G.neighbors(act_v))) == 1:
        return 1

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
                list(list_v + [n_i]),
                n_i
            )

    return int(len(neigh) - result < 2)
