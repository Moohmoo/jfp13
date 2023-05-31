"""Exercice 2.
"""

__authors__ = ["ZHUKOVA Nadezhda", "OUSSAREN Mohamed", "ROUAUD Lucas"]
__date__ = "31/05/2023"
__version__ = "0.0.1"
__copyright__ = "CC BY-SA"


import networkx as nx
import sys


def exercice_2(k, G):
    """Exercice 2. Get the shortest path between.

    Parameters
    ----------
    k : int
        Number of question.
    G : networkx.graph
        Networkx graph 
    """
    for i in range(k):
        u, v = input().split()

        shortest_path = nx.shortest_path(G, u, v)

        if len(shortest_path) > 2:
            print(f"{len(shortest_path) - 1} {shortest_path[1]}", flush=True)
        else:
            print(f"{len(shortest_path) - 1} {v}", flush=True)
