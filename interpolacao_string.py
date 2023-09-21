nome = "Pedro"
idade = 20
profissao = "Programador"
linguagem = "Python"

dados = {"nome" : "Pedro", "idade" : 20,"profissao":"Programador", "linguagem" : "Python"}

print("Olá, me chamo %s. Tenho %d anos, trabalho como %s e estrou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

print("Olá, me chamo {}. Tenho {} anos, trabalho como {} e estrou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {3}. Tenho {2} anos, trabalho como {1} e estrou matriculado no curso de {0}.".format(linguagem,profissao, idade, nome))

print(f"Olá, me chamo {nome}. Tenho {idade} anos, trabalho como {profissao} e estrou matriculado no curso de {linguagem}.")

print("Olá, me chamo {nome}. Tenho {idade} anos, trabalho como {profissao} e estrou matriculado no curso de {linguagem}.".format(**dados))
