"""Call other program.
"""

__authors__ = ["ZHUKOVA Nadezhda", "OUSSAREN Mohamed", "ROUAUD Lucas"]
__date__ = "31/05/2023"
__version__ = "0.0.1"
__copyright__ = "CC BY-SA"

import networkx as nx

from sys import exit as sysexit


from exercice_1 import exercice_1 as ex1
from exercice_2 import exercice_2 as ex2
from exercice_3 import exercice_3 as ex3
from exercice_4 import exercice_4 as ex4
from exercice_5 import exercice_5 as ex5


if __name__ == "__main__":
    # print(np.array(nx.find_cycle(G, orientation="ignore")))
    G = nx.Graph()

    with open("data/metro.txt", "r", encoding="utf-8") as file:
        for line in file:
            if line.strip() == "301 361":
                continue

            line = line.strip().split()
            G.add_edge(line[0], line[1])

    arg = input().split()

    if len(arg) != 2:
        sysexit("ERROR: Number of given arguments is incorrect")

    if arg[0] == "1":
        ex1(int(arg[1]))
    elif arg[0] == "2":
        ex2(int(arg[1]), G)
    elif arg[0] == "3":
        ex3(int(arg[1]), G)
    elif arg[0] == "4":
        ex4(int(arg[1]), G)
    elif arg[0] == "5":
        ex5(int(arg[1]))
    else:
        sysexit("ERROR: Given argument is incorrect. Unknown exercice.")
