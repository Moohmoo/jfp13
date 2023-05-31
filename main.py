"""Call other program.
"""

__authors__ = ["ZHUKOVA Nadezhda", "OUSSAREN Mohamed", "ROUAUD Lucas"]
__date__ = "31/05/2023"
__version__ = "0.0.1"
__copyright__ = "CC BY-SA"

from sys import argv
from sys import exit as sysexit

from exercice_1 import exercice_1 as ex1
from exercice_2 import exercice_2 as ex2
from exercice_3 import exercice_3 as ex3
from exercice_4 import exercice_4 as ex4
from exercice_5 import exercice_5 as ex5

if __name__ == "__main__":
    arg: list = argv

    if len(arg) != 3:
        sysexit("ERROR: Number of given arguments is incorrect.")

    if arg[1] == "1":
        ex1(arg[2])
    if arg[1] == "2":
        ex2(arg[2])
    if arg[1] == "3":
        ex3(arg[2])
    if arg[1] == "4":
        ex4(arg[2])
    if arg[1] == "5":
        ex5(arg[2])
    else:
        sysexit("ERROR: Given argument is incorrect. Unknown exercice.")
