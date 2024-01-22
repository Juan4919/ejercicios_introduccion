centavo = 1
cinco_centavos = 5
diez_centavos = 10
venticinco_centavos = 25
lunaticos = 100
toonies = 200

valor_introducido = int(input("Indica la cantidad a introducir en centavos > "))

cambio_toonies = valor_introducido // toonies
valor_introducido %= toonies

cambio_lunaticos = valor_introducido // lunaticos
valor_introducido %= lunaticos

cambio_venticinco_centavos = valor_introducido // venticinco_centavos
valor_introducido %= venticinco_centavos

cambio_diez_centavos = valor_introducido // diez_centavos
valor_introducido %= diez_centavos

cambio_cinco_centavos = valor_introducido // cinco_centavos
valor_introducido %= cinco_centavos

cambio_centavos = valor_introducido // centavo

print("Monedas toonies entregadas > ", cambio_toonies)
print("Monedas lunaticos entregadas > ", cambio_lunaticos)
print("Monedas de venticinco centavos entregadas > ", cambio_venticinco_centavos)
print("Monedas de diez centavos > ", cambio_diez_centavos)
print("Monedas de cinco centavos > ", cambio_cinco_centavos)
print("Monedas de un centavo entregadas > ", cambio_centavos)