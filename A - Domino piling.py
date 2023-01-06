# A - Domino piling
# url: https://codeforces.com/contest/50/problem/A

dim = input("")
dim_list = dim.split(" ")
dim_entero = [int(i)for i in dim_list]
espacio = dim_entero[0]*dim_entero[1]
domino = 2

if espacio % domino == 0:
  print(int(espacio/domino))
elif espacio % domino != 0:
  print(int((espacio-1)/2))
