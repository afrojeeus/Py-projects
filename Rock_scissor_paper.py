import random

import os

import re

os.system('cls' if os.name=='nt' else 'clear')

while (1 < 2):

    print('\n')

    print('Rock, Paper, Scissors - shoot!)

    userChoise = input("choose yout weapon [R]ock, [P]aper, or [S]cissors: ")

    of not re.match("[SsRrPp]", userChoice):

          print("Please choose Letter: ")

          print("[R]ock, [S]cissors 
