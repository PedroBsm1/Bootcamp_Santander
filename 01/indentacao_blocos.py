def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado")
        print("Retire seu dinheiro na boca do caixa.")

print("Obrigado por ser nosso cliente")
sacar(1000)

def depositar(valor):
    saldo = 500
    saldo += valor
