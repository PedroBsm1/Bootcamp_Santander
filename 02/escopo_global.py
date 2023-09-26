salario = 2000

def salario_bonus(bonus):
    global salario
    global lista_2
    salario += bonus
    lista.append(2)
    lista_2 = lista.copy()
    lista_2.append(3)
    return salario

lista = [1]
salario_com_bonus = salario_bonus(500)
print(salario_com_bonus)
print(lista)
print(lista_2)