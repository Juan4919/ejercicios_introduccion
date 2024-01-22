presion_kilopascales = float(input("Indica la presión en kilopascales > "))
libras_por_pulgada= presion_kilopascales/6.89476
mm_mercurio= presion_kilopascales*7.50062
atmosferas = presion_kilopascales/101.325

print("Libras por pulgada > ",libras_por_pulgada)
print("Milimetros de mercurio > ",mm_mercurio)
print("Atmosferas > ",atmosferas)

