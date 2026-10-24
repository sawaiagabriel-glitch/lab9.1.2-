from application.interfaces.i_conta_repository import IContaRepository
from domain.conta import Conta
from domain.cliente import Cliente


class ArquivoContaRepository(IContaRepository):

    def __init__(self, arquivo="contas.txt"):
        self.arquivo = arquivo

    def salvar(self, conta):
        contas = self._carregar_todas()

        contas[conta.cliente.cpf] = conta

        with open(self.arquivo, "w", encoding="utf-8") as arquivo:
            for cpf, conta_salva in contas.items():
                arquivo.write(
                    f"{conta_salva.cliente.nome}|"
                    f"{conta_salva.cliente.cpf}|"
                    f"{conta_salva.saldo}\n"
                )

    def buscar(self, cpf):
        contas = self._carregar_todas()

        cpf = cpf.strip()

        return contas.get(cpf)

    def _carregar_todas(self):
        contas = {}

        try:
            with open(self.arquivo, "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    linha = linha.strip()

                    if not linha:
                        continue

                    nome, cpf, saldo = linha.split("|")

                    cpf = cpf.strip()

                    cliente = Cliente(nome, cpf)
                    conta = Conta(cliente, float(saldo))

                    contas[cpf] = conta

        except FileNotFoundError:
            pass

        return contas