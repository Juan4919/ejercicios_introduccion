ancho=float(input("Introduce la longitud del campo en pies > "))
longitud=float(input("Introduce el ancho del campo en pies > "))

superficie_pies=ancho*longitud
superficie_acres=round(superficie_pies/43.560, 2)

print("La superficie del campo en acres es de",superficie_acres,"acres")
