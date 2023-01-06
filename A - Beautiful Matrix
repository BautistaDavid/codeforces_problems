# A - Beautiful Matrix - By: David Bautista - @PipeBau
# url: https://codeforces.com/contest/263/problem/A

dic1={}           # se crea un diccionario el cual contiene como keys a un numero de fila de la matriz,  
cont=0            # cada key esta asociado a una lista que contieen 5 numeros que fromaran pues un elemento de cada columna
cont2=0           # se crearon 3 contadores para poder llevar cuenta de los movimientos que se tendram que realizar
cont3=0
for i in range(5):  #se creo un bucle para generar los 5 inputs 
  x=input("")        #se nombran a los inputs 
  x=[int(j) for j in x.split(" ")]      #se transfroma la linea de texto ingresada al input a elementos en una lista 
  dic1[i+1]=x                           #se le asigna un numero a cada key, los cuales refieren a un numero de fila (1-5)
  for k in x:                       # si en el input aparece el numero 1 se registra la pocicion en la lista para asi determinar    
    if k==1:                         # cuantos el numero de movimientos entre columnas  
      cont=x.index(1)+1 
if cont!=3:
  p=3-cont
  cont3+=abs(p)         
for filas in dic1.keys():           #se cra un bucle anidado que accede a las combinaciones de numeros en el diccionario 
  for j in dic1[filas]:             # cuando reconosca que el numero es 1 el contador #3 registra el numero de movimientos entre   
    if j==1:                        # filas necesarios 
      if filas!=3:
        r=3-filas
        cont3+=abs(r)
print(cont3)
