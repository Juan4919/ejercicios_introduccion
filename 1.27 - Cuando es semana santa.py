def anonymous_gregorian_computus(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1

    return year, month, day

# Pedir el año al usuario
year_input = int(input("Ingrese el año para calcular la fecha de la Pascua: "))

# Llamar a la función para calcular la fecha de la Pascua
pascua_date = anonymous_gregorian_computus(year_input)

# Mostrar el resultado
print(f"La fecha de la Pascua en el año {pascua_date[0]} es el {pascua_date[2]} de {pascua_date[1]}")
