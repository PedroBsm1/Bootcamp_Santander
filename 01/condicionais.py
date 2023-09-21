MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade:"))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode ter CNH")

if idade < MAIOR_IDADE:
    print("Menor idade, não pode ter CNH")

if idade  >= MAIOR_IDADE:
    print("Maior de idade, pode ter CNH")
else:
    print("Menor idade, não pode ter CNH")


if idade  >= MAIOR_IDADE:
    print("Maior de idade, pode ter CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas")
else:
    print("Menor idade, não pode ter CNH")

saldo = 2000
saque = 250
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar saque")