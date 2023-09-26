def calcular_imposto(salario):
    aliquota = 0
    if(salario >= 0 and salario <= 1100.0):
        aliquota = 0.05
    elif(salario >= 1100.01 and salario <= 2500.0):
        aliquota = 0.10
    else:
        aliquota = 0.15
        
    return aliquota * salario

valor_salario = float(input("Qual o seu salario?: "))

valor_imposto = calcular_imposto(valor_salario)

saida = valor_salario - valor_imposto
print(f"{saida}")
