saldo_atual = int(input(100))
valor_deposito = float(input("Digite o valor do deposito: "))
valor_retirada = float(input("Digite o valor da retirada"))

#TODO: Calcular o saldo atualizado de acordo com a descrição deste desafio.
saldo_novo = (saldo_atual + valor_deposito) - valor_retirada
print(saldo_novo)