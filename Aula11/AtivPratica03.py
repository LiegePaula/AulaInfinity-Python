""" Crie uma classe Empresa que permita gerenciar
funcionários. Os funcionários devem ter informações
como nome, cargo e salário. A empresa deve ser capaz

de adicionar, remover e listar funcionários. """

class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f'{self.nome} - {self.cargo} - R${self.salario:.2f}'
    
class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionarFuncionario(self, funcionario):
        self.funcionarios.append(funcionario)
        print(f'Funcionario {funcionario.nome} adicionado com sucesso!')

    def removerFuncionario(self, nome):
        for f in self.funcionarios:
            if f.nome == nome:
                self.funcionarios.remove(f)
                print(f'Funcionerio {nome} removido com sucesso!')
                return
            
        print(f'Funcionario {nome} não encontrado.')

    def listarFuncionarios(self):
        if not self.funcionarios:
            print('Nenhum funcionarios cadastrado')
        else:
           print(f"\nLista de funcionários da empresa {self.nome}:")
        for f in self.funcionarios:
                print(f" - {f}") 

# Criando a empresa
empresa = Empresa("Tech Solutions")

# Criando funcionários
f1 = Funcionario("Ana", "Desenvolvedora", 5500)
f2 = Funcionario("Carlos", "Designer", 4200)
f3 = Funcionario("Marcos", "Gerente", 7000)

# Adicionando funcionários
empresa.adicionarFuncionario(f1)
empresa.adicionarFuncionario(f2)
empresa.adicionarFuncionario(f3)

# Listando funcionários
empresa.listarFuncionarios()

# Removendo um funcionário
empresa.removerFuncionario("Carlos")

# Listando novamente
empresa.listarFuncionarios()
