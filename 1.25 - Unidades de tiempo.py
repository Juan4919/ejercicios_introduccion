segundo = 1 
minuto = 60*segundo
hora = 60*minuto
dia = 24*hora
semana = 7*dia

segundos_entrada= float(input("Indica los segundos qu deseas calcular > "))

dias = segundos_entrada//dia
horas = (segundos_entrada%dia)//hora
minutos = (segundos_entrada%hora)//minuto
segundos = (segundos_entrada%minuto)//segundo

print(dias)
print(horas)
print(minutos)
print(segundos)