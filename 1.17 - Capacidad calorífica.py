'''
Q = mCAT

Q = cantidad total de energia (energia radiante)
m = masa
C = capacidad calorífica
AT = variacion de temperatura (termperatura final - temperatura inicial)
'''
 
nombre = input("¿Que materíal deseas comprobar? > ")
masa = (float(input("Introduce el peso (kg) o volumen (litros) > ")))*1000
capacidad = float(input("¿Que capacidad calorífica tiene el material que deseas comprobar? > ")) 
variacion_de_temperatura = float(input("Indica los grados de temperatura que deseas aumentar o reducir > "))

cantidad_energia = masa*capacidad*variacion_de_temperatura
print()
print(f"La capacidad calórifica del material indicado '{nombre}', es {cantidad_energia} julios, lo que serían {cantidad_energia/4186} calorías")
print()
valor_kwh = 0.00000027777777777777776
kwh = cantidad_energia*valor_kwh
precio_kwh = kwh * 0.089 #centavos por kw/h

print(f"El coste de calentar {masa} de '{nombre}', sería de {precio_kwh} centavos por hora.")
print()