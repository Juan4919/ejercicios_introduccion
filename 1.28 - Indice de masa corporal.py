altura_cm = float(input("Indica la altura en cm > "))
peso = float(input("Indica el peso en kg > "))
altura_m = altura_cm/100

imc = round(peso/(altura_m**2), 2) 

print(f"tu IMC es > {imc}")