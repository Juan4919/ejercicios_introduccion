from math import pi

radio= float(input("Indíca el radio del cilindro en cm > "))
altura= float(input("Indica la altura del cilindro en cm > "))
volumen= round(pi*((radio**2)*altura), 1)

print("El volumen del cilindro es",volumen,"cm3")


