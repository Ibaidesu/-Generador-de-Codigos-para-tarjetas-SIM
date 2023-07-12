#!/usr/ python3
#generador de codigos PIN aleatorios para Tarjeta SIM
from random import choice
length = 4
value = "334567854335809054311346780087563134560808967784511023694"

print ("El Codigo PIN Generado para su Tarjeta SIM es el Siguiente...")
p = ""
p = p.join([choice(value) for i in range(length)])
print(p)


#!/generador de codigos pin aleatorios para Tarjeta SIM
