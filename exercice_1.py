"""Exercice 1.
"""

__authors__ = ["ZHUKOVA Nadezhda", "OUSSAREN Mohamed", "ROUAUD Lucas"]
__date__ = "31/05/2023"
__version__ = "0.0.1"
__copyright__ = "CC BY-SA"

from data.metro import graph
from tqdm import tqdm
import sys


def exercice_1(k):
    """Exercice 1: check if two nodes are connected.

    Parameters
    ----------
    k : int
        Number of asked questions.
    """
    for i in range(k):
        u, v = input().split()

        u = int(u)
        v = int(v)

        is_neighbor: int = 0

        if v in graph[u]:
            is_neighbor = 1

        print(is_neighbor, flush=True)
