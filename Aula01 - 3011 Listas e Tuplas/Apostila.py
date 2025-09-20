for i in range(6):
    print(i)
#break no for   
numero_procurado = 9
for i in range(1,10):
    if i == numero_procurado:
        print('Achei')
        break
    print(i)

#Continue no for
for i in range(1,11):
    if i % 2 != 0:
        continue
    print(i)
#break e continue
for num in range(2,20):
    for i in range(2, num):
        if num % 1 ==0:
            break
    else:
        print(f'{num} e um primo!')
#Listas e suas caracteristicas
#exemplos de listas:
#lista de numeros:
lista_de_numeros = [1,2,3,4,5]
#lista de letras:
lista_de_letras = ['a','b','c','d','e']
#lista de valores logicos
lista_de_logicos = [True, False, False, True]
#lista com diferentes tipos de dados
lista_mista = ['Gabriel', 12, True]
#posição de elemento em uma lista
notas = [10.0, 9.8, 8.7]
print(notas)
print(notas[1])    
#posição de elementos do final
letras = ['a','b','c','e','f']
print(letras[-1])
print(letras[-2])
print(letras[-3])
print(letras[-4])
print(letras[-5])

#Finalidade
#Adição de itens = .append() / adicionar um elemento ao final da lista
#Adição de itens = .insert() / adicionar um elemento na posição informada
#Remoção de itens = .remove() / remover um elemento de uma lista atraves de seu valor
#Remoção de itens = .pop() / remover um elemento de uma lista atraves de seu indice

#adicionar item ao final da lista .append()
numeros = [1,2,3,4,5]
print(numeros)
numeros.append(6)
print(numeros)
#adicionar item em dada posição da lista .insert()
numeros =[10,30,40,50]
print(numeros)
letras = ['a','e','o','u']
print(letras)
pesos = [1.2, 3.4, 5.3, 6.7]
print(pesos)
#inserindo
numeros.insert(1,20)
letras.insert(2,'i')
pesos.insert(2,4.0)

print(numeros)
print(letras)
print(pesos)
# Exclusaõ de itens
notas = [
    9.0,
    8.7,
    9.9,
    8.7,
    7.9
]
print(notas)
notas.pop(0)
print(notas)
notas.pop(1)
print(notas)
notas.pop(2)
print(notas)

lista_nomes = [
    'Maria',
    'Pedro',
    'Ana',
    'Joao',
    'Laura'
]
print(lista_nomes)
lista_nomes.remove('Ana')
print(lista_nomes)
lista_nomes.pop(2)
print(lista_nomes)

# iterando listas com FOR

#definição Lista de compras
lista_compras = [
    '2 pct Arroz',
    '2 pct Feijão',
    '2 pct Farinha de Mandioca',
    '4 kg Linguiça Calabresa',
    '4 kg de Charque',
    '2 kg Bacon de barriga',
    '2 kg de Laranja',
]
print('LISTA DE COMPRAS', end = '\n\n')

for item in lista_compras:
    print('[ ]', item)

# Tuplas, são listas imutáveis
# Listas e Tuplas

# Listas mutáveis
minha_lista = [1,2,3,4,5]
print(minha_lista)
minha_lista[0] = 10
print(minha_lista)
minha_lista.append(6)
print(minha_lista)

# Tupla imutável
minha_tupla = (11,12,13,14,15)
print(minha_tupla)
# minha_tupla[0] = 10
print(minha_tupla)

# Criando uma Tupla
frutas = ('maça', 'Banana', 'Banana', 'Laranja', 'Abacaxi', 'Banana')
print(frutas)
# Metodo index(): Retorna o índice do primerio elemento especificado
indice_laranja = frutas.index('Laranja')
print('Indice Laranja', indice_laranja)

# Metodo count(): Retorna o numero de ocorrencias de um elemento
quantidades_bananas = frutas.count('Banana')
print('Quantidades de banana', quantidades_bananas)

# Descompactando uma Tupla: DEU ERRADP
(maca, banana, laranja, abacaxi) = frutas 
print('Fruta 1:', maca)
print('Fruta 2:', banana)
print('Fruta 3:', laranja)
print('Fruta 4:', abacaxi)

