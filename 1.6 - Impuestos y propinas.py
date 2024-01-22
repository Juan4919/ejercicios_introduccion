valor_comida=float(input("¿Cual es el valor bruto de la comida? > "))
impuesto=float(input("¿Cuanto es el impuesto establecido? > "))
propina=int(18) #La propina es el 18%
valor_propina=round(((valor_comida/100)*18),2)
comida_y_propina=round(valor_comida+valor_propina, 2)
valor_impuesto=round((comida_y_propina/100)*impuesto, 2)
print()
print("El valor de la comida es de",valor_comida,"€, con una propina de",propina,"%, que sería",valor_propina,"€, que al aplicarle un impuesto del",impuesto,"%,")
print("nos da un total de",comida_y_propina+valor_impuesto,"o lo que es lo mismo,",comida_y_propina,"€ por la comida y la propina, y",valor_impuesto,"€, de impuestos")