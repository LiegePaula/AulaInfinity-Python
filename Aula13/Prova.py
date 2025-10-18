""" Crie uma classe chamada ContaBancaria que tenha dois atributos privados, _saldo e _titular. O atributo _saldo deve armazenar o saldo da conta, enquanto o atributo _titular deve armazenar o nome do titular da conta. Para interagir com esses atributos, implemente métodos públicos que permitam realizar operações bancárias. Crie um método depositar que permita adicionar um valor ao saldo, um método sacar que permita retirar um valor do saldo (caso haja saldo suficiente), e um método exibir_saldo que exiba o saldo atual da conta. Utilize métodos para encapsular o acesso ao saldo, garantindo que ele só possa ser alterado de maneira controlada pelos métodos de depósito e saque. """

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular
        self._saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f'Deposito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('Valor de deposito inválido. Informe um valor positivo.')

    def sacar(self, valor):
        if valor <= 0:
            print('Valor de saque inválido. Informe um valor positivo.')
        elif valor > self._saldo:
            print('Saldo insuficiente para realizar o saque.')
        else:
            self._saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso.')

    def exibir_saldo(self):
        print(f'Titular: {self._titular}')
        print(f'Saldo atual: R$ {self._saldo:.2f}')

conta1 = ContaBancaria('Liege', 1000)

conta1.exibir_saldo()
conta1.depositar(500)
conta1.exibir_saldo()
conta1.sacar(200)
conta1.exibir_saldo()
conta1.sacar(2000)
conta1.exibir_saldo()



