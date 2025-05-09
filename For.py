#Primeira etapa - Criar uma lista com 5 itens
objetos = ["base", "lapis", "caneta", "garrafa", "brinco"]
print("lista de objetos criada")

#Segunda etapa - Adicione mais um objeto ao final da lista
objetos.append("caixa")
print("item adicionado com sucesso")

#Terceira etapa - Acesse o objeto que está na 2 posição.
acesso = objetos[2]
print(f" {acesso} item acessado com sucesso")

#Quarta etapa - Remova um objeto da lista.
objetos.remove("base")
print("item removido com sucesso")

#Quinta etapa - Exiba o tamanho da lista.
len(objetos)
print(len(objetos))
print("tamanho da lista exibido com sucesso")


#Sexta etapa - Mostre todos os itens com um laço for.
for objeto in objetos:
    print(objeto)
print("item mostrado com sucesso")

# Setima etapa - Mostre todos os itens com um laço for.
if "cadeira" in objetos:
    objetos.remove("cadeira")
    print("item removido com sucesso")
else:
    objetos.append("cadeira")
    print("cadeira adicionada com sucesso")
print("item verificado e adicionado ou removido com sucesso")

#Oitava etapa - Mostre todos os itens com um laço for.
objetos.sort()
print("lista em ordem alfabetica com sucesso")

#Nona etapa - Mostre todos os itens com um laço for.
primeiro = objetos[0]
ultimo =  objetos[-1]
print(primeiro)
print(ultimo)
print("primeiro e ultimo item mostrado com sucesso")

#Desima etapa - Limpe toda a lista
objetos.clear()
print(objetos)
print("todos os itens removidos")
