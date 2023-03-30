class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia
        print(f'Iniciando sistema saldo disponível: {saldo}')

    def depositar(self, valor):
        # ...
        self._saldo += valor
        return f'deposito realizado no valor {valor}'

    def sacar(self, valor):
        # ...
        self._saldo -= valor
        return f'Saque realizado no valor {valor}'

    def mostrar_saldo(self):
        # ...
        return f'saldo disponível {self._saldo}'


conta = Conta('7384', 5500)
print(conta.depositar(500))
print(conta.mostrar_saldo())
print(conta.sacar(1500))
print(conta.mostrar_saldo())
