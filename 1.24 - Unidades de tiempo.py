dias = float(input("Indica los días > "))
horas = float(input("Indica las horas > "))
minutos = float(input("Indica los minutos > "))
segundos = float(input("Indica los segundos > "))

segundos_total = (dias*24*60*60)+(horas*60*60)+(minutos*60)+segundos

print("El tiempo total en segundos es > ",segundos_total)