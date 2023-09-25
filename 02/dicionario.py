pessoa = dict(nome="Guilherme", idade = 28)
pessoa["telefone"] = "988053465"

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["telefone"])


pessoas = {
    "guilherme@gmail.com" : {"nome" : "Guilherme", "idade" : "28", "telefone" : "988053465"},
    "antonio@gmail.com": {"nome" : "antonio", "idade" :"42", "telefone" : "12039102312"},
    "amanda@gmail.com":{"nome" : "amanda", "idade" : "39", "telefone" : "123213123"},
}

for chave in pessoas:
    print(chave, pessoas[chave])

#pessoas.clear()
copia = pessoas.copy()
copia["guilherme@gmail.com"] = {"nome":"GUI"}
print(pessoas["guilherme@gmail.com"])
print(copia["guilherme@gmail.com"])

#dict.fromkeys(["nome", "telefone"], "vazio")

print(pessoas.get("guilherme@gmail.com"))
print(pessoas.items())

contato = {"nome" : "Guilherme", "idade" : "28", "telefone" : "988053465"}
print(contato.setdefault("nome", "Giovana"))

contato.update({
    "guilherme@gmail.com" : {"nome" : "Gui"}
})

contato.update({
    "Giovana@gmail.com" : {"nome" : "Giovana", "idade" : "28", "telefone" : "988053465"}
})

resultado = "Giovana@gmail.com" in contato
print(resultado)

del contato["guilherme@gmail.com"]["telefone"]
del contato["Giovana@gmail.com"]