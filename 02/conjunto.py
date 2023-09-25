lista = ([1,2,3,3,2,5,4])
print(set(lista))

carros = set(("palio", "ecosport", "X1", "civic", "civic", "palio"))
print(carros)


conjunto_a = {1, 2, 3}
conjunto_b = {3,4,5,6}

print(conjunto_a.union(conjunto_b))
print(conjunto_a.intersection(conjunto_b))
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))
print(conjunto_a.symmetric_difference(conjunto_b))
print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))
print(conjunto_b.issuperset(conjunto_a))
print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.add(90))
print(conjunto_a.discard(1))
print(conjunto_a.pop())