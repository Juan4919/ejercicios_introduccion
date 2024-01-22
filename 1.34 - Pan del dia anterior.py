hogaza = 3.49
descuento_pan_anterior = 0.60
pan_comprado=float(input("Indica el número de hogazas de pan del día anterior que deseas > "))
precio_pan=round(pan_comprado*hogaza, 2)
print()
print(f"El precio habitual de las hogazas compradas es {precio_pan}€")
print(f"Al tratarse de pan del día anterior, el descuento aplicado son {round(precio_pan*descuento_pan_anterior,2)}€")
print(f"El precio final a pagar será de {round(precio_pan-precio_pan*descuento_pan_anterior,2)}€")