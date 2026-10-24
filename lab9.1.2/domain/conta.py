from datetime import datetime


class Conta:
    def __init__(self, cliente, saldo=0, historico=None):
        self.cliente = cliente
        self.saldo = saldo
        self._historico = historico or []

    def depositar(self, valor):
        self.saldo += valor

        self._historico.append({
            "tipo": "Deposito",
            "valor": valor,
            "data": datetime.now()
        })

    def sacar(self, valor):
        self.saldo -= valor

        self._historico.append({
            "tipo": "Saque",
            "valor": valor,
            "data": datetime.now()
        })

    @property
    def historico(self):
        return self._historico