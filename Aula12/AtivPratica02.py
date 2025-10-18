""" Crie uma hierarquia de classes que represente veículos. Comece com uma classe base "Veículo" e, em seguida,crie classes derivadas como "Carro" e
"Bicicleta." Adicione métodos para definir atributos, como "cor"
e "modelo, " e permita a chamada de métodos em cadeia para
configurar esses atributos. """

class Veiculo:
    def __init__(self):
        self.cor = None
        self.modelo = None


    def set_cor(self, cor):
        self.cor = cor
        return self  

    
    def set_modelo(self, modelo):
        self.modelo = modelo
        return self  
    
    def exibir_info(self):
        print(f"Veículo: {self.__class__.__name__}")
        print(f"Cor: {self.cor}")
        print(f"Modelo: {self.modelo}")
        print("-" * 30)

class Carro(Veiculo):
    def __init__(self):
        super().__init__()

class Bicicleta(Veiculo):
    def __init__(self):
        super().__init__()

carro = Carro().set_cor("Vermelho").set_modelo("Sedan")
bicicleta = Bicicleta().set_cor("Azul").set_modelo("Speed")

carro.exibir_info()
bicicleta.exibir_info()