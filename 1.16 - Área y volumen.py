from math import pi

radio = float(input("Indica la medida de radio > "))
area = round(pi*radio*2,2)
volumen = round((4/3)*(pi*radio**3),2)

print(f"El área del circulo es {area}, mientras que el volumen es {volumen}")