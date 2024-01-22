'''
área = norte*s2 / 4*tan(pi/n)
'''
from math import pi, tan

longitud_lado = float(input("Indica la longitud de un lado en cm > "))
numero_lados = float(input("Indica el número de lados del polígono > "))

area = (numero_lados*(longitud_lado**2))/(4*tan(pi/numero_lados))

print(round(area,2),"CM")