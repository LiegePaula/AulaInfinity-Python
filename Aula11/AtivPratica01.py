class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

# Criando um objeto da classe Cachorro
meu_cachorro = Cachorro("Rex", "Labrador", 3)

# Exibindo os atributos
print("Nome:", meu_cachorro.nome)
print("Raça:", meu_cachorro.raca)
print("Idade:", meu_cachorro.idade)

