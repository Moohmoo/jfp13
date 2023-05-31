"""Exercice 4.
"""

__authors__ = ["ZHUKOVA Nadezhda", "OUSSAREN Mohamed", "ROUAUD Lucas"]
__date__ = "31/05/2023"
__version__ = "0.0.1"
__copyright__ = "CC BY-SA"

import sys
import random

def exercice_4(k, G):
    for _ in range(k):
        pos_gen1, pos_gen2 = 0, 0
        score = 0
        rondes = 100
        for i in range(rondes) :
            print(i, file=sys.stderr)
            if i == 0:
                corespondance = sorted(G.degree, key=lambda x: x[1], reverse=True)[0:50]
                pos_gen1 = str(random.choice(corespondance)[0])
                pos_gen2 = str(random.choice(corespondance)[1])
                print(pos_gen1, pos_gen2, file=sys.stderr)
            else :
                pos_gen1 = str(list(G.neighbors(pos_gen1))[0])
                pos_gen2 = str(list(G.neighbors(pos_gen2))[0])
            print(pos_gen1 + " " + pos_gen2, flush=True)
            v = input()
            if v == -1:
                score = (101 - rondes) * 10
            elif v == -2 and i == rondes - 1:
                score = 0
            # print(i, file=sys.stderr)
