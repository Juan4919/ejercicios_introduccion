numero = int(input("Ingrese un número entero: "))
numero_str = str(numero)
suma_digitos = sum(int(digito) for digito in numero_str)
print(f"La suma de los dígitos es: {'+'.join(numero_str)} = {suma_digitos}")
