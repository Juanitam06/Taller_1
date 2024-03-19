
#programa para generar un numero aleatorio

import random

a= input("Limite inferior: ")
b= input("Limite superior: ")

#convertir a y b a enteros
a= int(a)
b= int(b)
respuesta= random.randint(a,b)
print(respuesta)
