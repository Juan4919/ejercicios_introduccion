'''
WCI = 13,12 + 0,6215Ta - 11,37V0,16+ 0,3965TaV0,16
Ta = temperatura aire 
V = velocidad del viento en km/h
'''

temperatura_aire= float(input("Indica la temperatura del aire > "))
velocidad_aire = float(input("Indica la velocidad del aire > "))

sensacion_termica = 13.12 + 0.6215 * temperatura_aire - 11.37 * (velocidad_aire**0.16) + 0.3965 * temperatura_aire * (velocidad_aire**0.16)

print(f"La sensación termica es > {sensacion_termica}")