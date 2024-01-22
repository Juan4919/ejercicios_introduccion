latas_1l=int(input("Indica el número de botellas de 1L o menos que deseas entregar > "))
latas_2l=int(input("Indica el número de botellas de mas de 1L que deseas entregar > "))

valor_latas_1l=latas_1l*0.10
valor_latas_2l=latas_2l*0.25

valor_total=round(valor_latas_1l+valor_latas_2l, 2) 

print("El valor total de las latas entregadas es de",valor_total,"$")
