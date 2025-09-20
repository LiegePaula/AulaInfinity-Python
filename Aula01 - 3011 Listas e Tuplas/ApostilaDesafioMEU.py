# Suponha que você está gerenciando uma competição esportiva e tem uma lista de tuplas
# representando os resultados das equipes em diferentes modalidades. Cada tupla contém 
# o nome da equipe, seguido por uma lista de pontuações obtidas em cada rodada da 
# competição.

# 1.Calcule a média das pontuações de cada equipe e armazene esses valores em uma nova 
# lista chamada medias.
# 2.Ordene a lista medias em ordem decrescente.
# 3.Crie uma nova lista chamada classificacao que contém tuplas, onde
# cada tupla contém o nome da equipe e sua média de pontuações.
# 4.Exiba na tela a  final das equipes, mostrando o nome da
# equipe e sua média, da equipe com a pontuação mais alta para a mais baixa.

equipe1 = ('Basquete', 72, 84, 90)
equipe2 = ('Volei', 25, 25, 25)
equipe3 = ('Futsal', 43, 45, 38)
#1
medias = []
pontos1 = equipe1[1:]
#print(pontos1)
soma1 = 0
contador1 = 0
for i in pontos1:
    soma1 = soma1 + i
    contador1 += 1
media1 = soma1 / contador1
#print(media1)
medias.append(media1)
#print(medias)

pontos2 = equipe2[1:]
#print(pontos2)
soma2 = 0
contador2 = 0
for i in pontos2:
    soma2 = soma2 + i
    contador2 += 1
media2 = soma2 / contador2
#print(media2)
medias.append(media2)
#print(medias)

pontos3 = equipe3[1:]
#print(pontos3)
soma3 = 0
contador3 = 0
for i in pontos3:
    soma3 = soma3 + i
    contador3 += 1
media3 = soma3 / contador3
#print(media3)
medias.append(media3)
print(f"A media das pontuações é {medias}")
#2
medias.sort(reverse=True)
print(f'As medias das pontuações em ordem decrescente é {medias}.')
medias_decrescente = sorted(medias,reverse=True)
print(f'As medias das pontuações em ordem decrescente é {medias_decrescente}.')

#3.Crie uma nova lista chamada classificacao que contém tuplas, onde
# cada tupla contém o nome da equipe e sua média de pontuações.

classificação = [
    (equipe1[0], media1),
    (equipe2[0], media2),
    (equipe3[0], media3)
]
print(classificação)

# 4.Exiba na tela a  final das equipes, mostrando o nome da
# equipe e sua média, da equipe com a pontuação mais alta para a mais baixa.

final_das_equipes = sorted(classificação, key=lambda x: x[1], reverse=True)
print(final_das_equipes)