numero1=float(input("Introduce el primer numero > "))
numero2=float(input("Introduce el segundo numero > "))
numero3=float(input("Introduce el tercer numero > "))

minimo=min(numero1,numero2,numero3)
maximo=max(numero1,numero2,numero3)
intermedio=numero1+numero2+numero3-maximo-minimo

print(f"El número minimo es {minimo}, el intermedio {intermedio} y el máximo es {maximo}")