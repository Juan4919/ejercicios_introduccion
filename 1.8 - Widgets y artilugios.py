widget_peso = 75
aparato_peso= 112

cantidad_widgets=int(input("Indica el número de widgets que deseas comprar > "))
cantidad_artilugios=int(input("Indica el número de aparatos que quieres comprar > "))
peso_total=(cantidad_widgets*widget_peso)+(cantidad_artilugios*aparato_peso)
print()
print(widget_peso)
print(f"El peso total de todos los {cantidad_widgets} widgets y los {cantidad_artilugios} artilugios sería de {peso_total} gramos")