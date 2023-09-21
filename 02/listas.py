frutas = ["laranja", "maça", "uva"]
letras = list("python")
numero = list(range(10))
carro = ["Ferrari", "f8", 4200000, 2020, 2900, "São Paulo", True]
print(frutas)
print(letras)
print(numero)
print(carro)


matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]
print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])


lista = ["p", "y", "t", "h", "o", "n"]
print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])

for letter in  lista:
    print(letter)

numeros = [1, 30, 40, 12, 24, 55, 9]
quadrado = []

for numero in numeros:
    quadrado.append(numero**2)

print(quadrado)

quadrado = (numero ** 2 for numero in numeros)

