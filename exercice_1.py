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
    for question in range(k):
        print(question, file=sys.stderr)
        u, v = input(f"Question #{question}: ").split()

        u = int(u)
        v = int(v)

        print(f"{u=} {v=}", file=sys.stderr)

        is_neighbor: int = 0

        if v in graph[u]:
            is_neighbor = 1

        print(is_neighbor, flush=True)
