def somar_numeros(*args):
    resultado = 0
    for num in args:
        resultado += num
    return resultado

print(somar_numeros(1,2,3))
print(somar_numeros(5,8,7,6,20))

def mostrar_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}:{valor}')

mostrar_info(nome='João', idade=30, cidade='Belo Horizonte')

def mostrar_informacoes(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}:{valor}')

mostrar_informacoes(nome='Alice', idade=30, cidade='Belo Horizonte')

mostrar_informacoes(curso='Python', nivel='Iniciante', plataforma='Online')

def minha_funcao(*args, **kwargs):
    for arg in args:
        print(arg)
    for chave, valor in kwargs.items():
        print(chave, valor)

minha_funcao('Curriculo', 'Desenvolvimento', nome = 'Alice', idade=25)

variável = lambda parâmetro : comando


quadrado = lambda x : x **2
print(quadrado(5))

par = lambda y: y % 2 == 0
print(par(10))

name_upperCase = lambda n : n.upper()
print(name_upperCase('Jose'))

par_impar = lambda x: "par" if x % 2 == 0 else 'ímpar'
print(par_impar(5))
print(par_impar(-2))


valida_usuarios = lambda user: 'Erro: usuario precisa ser definido' if user == '' else('usuario não pode ter menos de 4 digitos' if len(user) < 4 else 'usuario definido com sucesso!' )
print(valida_usuarios(''))
print(valida_usuarios('ze'))
print(valida_usuarios('jose'))

numeros = [1,2,3,4,5]
quadrados = list(map(lambda x: x **2, numeros))
print(quadrados)

from functools import reduce

numeros = [1,2,3,4,5]
soma = reduce(lambda x, y: x + y, numeros)
print(soma)


