#texto = input ("Informe um texto:")
#VOGAIS = "AEIOU"

#for letra in texto:
  #  if letra.upper() in VOGAIS:
 #       print(letra, end="")
#else:
  #  print()


#for numero in range(0, 51,5): #0 start / 51 stop / 5 step
 #   print(numero, end=" ")


opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n:"))
    if opcao == 1:
        print ("Sacando...")
    elif opcao ==2:
        print("Exibindo extrato...")
else:
    print("Obrigado por usar nosso sistema bancário.")


while True:
    numero = int(input("Informe um número:"))

    if numero == 10:
        break

    print(numero)

for numero in range(100):
    if numero == 12:
        break

    print(numero, end=" ")

for numero in range(100):
    if numero == 12:
        continue

    print(numero, end=" ")