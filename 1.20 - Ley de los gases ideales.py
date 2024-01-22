'''
PV=nRT

P = Presion en pascales
V = Volumen en litros 
n = capacidad de sustancia J en moles
R = constante de gases ideales (8,314)
T = mol K, temperatura en grados kelvind
'''

presion = float(input("Indica la presión > "))
volumen = float(input("Indíca el volumen > "))
temperatura = float(input("Indíca la temperatura en grados centígrados > "))
temperatura_kelvin = temperatura+273.15
gas_ideal= presion*volumen*temperatura_kelvin

print(gas_ideal)