# Suponha que você está gerenciando uma competição esportiva e tem
# uma lista de tuplas representando os resultados das equipes em
# diferentes modalidades. Cada tupla contém o nome da equipe, seguido
# por uma lista de pontuações obtidas em cada rodada da competição.

# 1.Calcule a média das pontuações de cada equipe e armazene esses
# valores em uma nova lista chamada medias.
# 2.Ordene a lista medias em ordem decrescente.
# 3.Crie uma nova lista chamada classificacao que contém tuplas, onde
# cada tupla contém o nome da equipe e sua média de pontuações.
# 4.Exiba na tela a  final das equipes, mostrando o nome da
# equipe e sua média, da equipe com a pontuação mais alta para a
# mais baixa.

equipe1 = ('Basquete', 72, 84, 90)
equipe2 = ('Volei', 25, 25, 25)
equipe3 = ('Futsal', 43, 45, 38)
medias = []

pontos1 = equipe1[1:]
soma1 = 0
contagem1 = 0
for ponto in pontos1:   
    soma1 += ponto
    contagem1 += 1
media1 = soma1 / contagem1 if contagem1 > 0 else 0
medias.append(media1)

pontos2 = equipe2[1:]
soma2 = 0
contagem2 = 0
for ponto in pontos2:   
    soma2 += ponto
    contagem2 += 1
media2 = soma2 / contagem2 if contagem2 > 0 else 0
medias.append(media2)


pontos3 = equipe3[1:]
soma3 = 0
contagem3 = 0
for ponto in pontos3:   
    soma3 += ponto
    contagem3 += 1
media3 = soma3 / contagem3 if contagem3 > 0 else 0
medias.append(media3)
print(medias)

medias_decrescente = sorted(medias, reverse=True)
print(medias_decrescente)

classificação = [
    (equipe1[0],media1),
    (equipe2[0], media2), 
    (equipe3[0], media3)
    ]

print(classificação)

classificação.sort()
print(classificação)

