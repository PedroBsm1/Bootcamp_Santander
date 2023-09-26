#def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
#    print(modelo, ano, placa, marca, motor, combustivel)

#criar_carro("Palio", 1999, "ABC-1234", "Fiat", '1.0', "Gasolina")
#criar_carro("Palio", 1999, "ABC-1234", marca= "Fiat", motor='1.0', combustivel= "Gasolina")

def somar (a, b):
    return a + b

def subtrair (a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao (a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10,10, somar)
exibir_resultado(10,10, subtrair)

operacao = somar

print(operacao(1,2))