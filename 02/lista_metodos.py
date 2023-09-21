lista = []
lista.append(1)
lista.append("Python")
lista.append([40, 30, 12])

print (lista)
#lista.clear()
#print (lista)

lista2 = lista.copy()
lista2.append(123)

print(lista)
print(lista2)


cores = ["Vermelho", "azul", "cinza"]
print(cores.count("Vermelho"))
print(cores.count("amarelo"))

cores.extend(["verde", "amarelo", "preto"])
print(cores)

print(cores.index("azul"))

print(cores)
cores.pop()
print(cores)
cores.pop(0)
print(cores)

cores.remove("amarelo")
print(cores)
cores.reverse()
print(cores)

cores2 = ["Vermelho", "azul", "cinza", "verde", "amarelo", "preto"]
cores2.sort()
print(cores2)

cores2 = ["Vermelho", "azul", "cinza", "verde", "amarelo", "preto"]
cores2.sort(reverse=True)
print(cores2)

cores2 = ["Vermelho", "azul", "cinza", "verde", "amarelo", "preto"]
cores2.sort(key=lambda x: len(x))
print(cores2)

cores2 = ["Vermelho", "azul", "cinza", "verde", "amarelo", "preto"]
cores2.sort(key=lambda x: len(x), reverse = True)
print(cores2)

print(len(cores2))


[n**2 if n > 6 else n for n in range(10) if n % 2 == 0]

print(n)