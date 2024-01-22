'''
vf = v2 + 2ad

vf = velocidad final
vi = velocidad inicial 
a = aceleracion 
d = distancia

'''

distancia = float(input("Indica la distancia o altura desde la que cae el objeto > ")) #expresada en metros
aceleracion = 9.8 
velocidad_inicial = 0
velocidad_final = (velocidad_inicial**2)+2*aceleracion*distancia

print(f"La velocidad final es {velocidad_final**0.5} m/s")