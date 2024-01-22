'''
área = s * (s-s1)*(s-s2)*(s-s3)
'''

lado1 = float(input("Introduce la medida de lado 1 > "))
lado2 = float(input("Introduce la medida de lado 2 > "))
lado3 = float(input("Introduce la medida de lado 3 > "))

superficie = (lado1 + lado2 + lado3)/2
area = superficie*(superficie-lado1)*(superficie-lado2)*(superficie-lado3)

print(f"el área es {area}")
print()
print(f"la superficie es {superficie}")