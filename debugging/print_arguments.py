#!/usr/bin/python3
import sys

# Commencer la boucle à partir de l'indice 1 pour éviter sys.argv[0]
for i in range(1, len(sys.argv)):
    print(sys.argv[i])
