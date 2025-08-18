lista = []
#acrescenta no final da minha lista
# CREATE => CRIAR
#CREAT criando 
print(lista)
lista.append('Tião')
lista.append('Maria')

print(lista)
print(len(lista))
lista.insert(0,'Jose')
lista.insert(10,'Jose')
lista.append('liege')

#READ lendo os elementos
print(lista)
print(len(lista))

#UPDATE atualizando

lista[3] = 'Jose da lapa'
print(lista)

#DELETE

lista.pop() #remove ultimo elemento -1 é o ultimo elemento da lista
print(lista)

lista.pop(0)
print(lista)

# remove o conteudo da lista
lista.remove('maria'.capitalize())
print(lista[0].upper())




#CRUD
#CREAT criando 
#READ lendo os elementos
#UPDATE atualizando
#DELETE  deletando/apagando

#alt + shift + seta pra baixo

cpf = ('01399505670',)
print(cpf)
print(type(cpf))


