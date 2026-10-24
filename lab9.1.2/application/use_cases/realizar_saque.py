class RealizarSaqueUseCase:

    def __init__(self, repository):
        self.repository = repository

    def executar(self, cpf, valor):
        conta = self.repository.buscar(cpf)

        if conta is None:
            raise ValueError("Conta não encontrada.")

        if valor <= 0:
            raise ValueError("O valor deve ser maior que zero.")

        if valor > conta.saldo:
            raise ValueError("Saldo insuficiente.")

        conta.sacar(valor)

        self.repository.salvar(conta)

        return conta