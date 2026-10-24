import tkinter as tk
from tkinter import messagebox

from domain.cliente import Cliente
from domain.conta import Conta


class ContaView:
    def __init__(self, root, repository, deposito_use_case, saque_use_case):
        self.root = root
        self.repository = repository
        self.deposito_use_case = deposito_use_case
        self.saque_use_case = saque_use_case

        self.root.title("Gerenciamento Bancário")
        self.root.geometry("430x520")

        # Nome
        tk.Label(root, text="Nome:").pack(pady=5)

        self.nome_entry = tk.Entry(root)
        self.nome_entry.pack()

        # CPF
        tk.Label(root, text="CPF:").pack(pady=5)

        self.cpf_entry = tk.Entry(root)
        self.cpf_entry.pack()

        # Saldo inicial
        tk.Label(root, text="Saldo Inicial:").pack(pady=5)

        self.saldo_entry = tk.Entry(root)
        self.saldo_entry.pack()

        # Criar conta
        tk.Button(
            root,
            text="Criar Conta",
            command=self.criar_conta
        ).pack(pady=10)

        # Buscar conta
        tk.Button(
            root,
            text="Buscar Conta",
            command=self.buscar_conta
        ).pack(pady=5)

        # Área para mostrar a conta
        self.resultado = tk.Label(
            root,
            text="",
            justify="left"
        )
        self.resultado.pack(pady=10)

        # Valor da operação
        tk.Label(
            root,
            text="Valor da operação:"
        ).pack(pady=5)

        self.valor_entry = tk.Entry(root)
        self.valor_entry.pack()

        # Botões de depósito e saque
        frame_botoes = tk.Frame(root)
        frame_botoes.pack(pady=10)

        tk.Button(
            frame_botoes,
            text="Depositar",
            command=self.depositar
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            frame_botoes,
            text="Sacar",
            command=self.sacar
        ).pack(side=tk.LEFT, padx=5)

    def criar_conta(self):
        try:
            nome = self.nome_entry.get().strip()
            cpf = self.cpf_entry.get().strip()
            saldo_texto = self.saldo_entry.get().strip()

            if not nome:
                raise ValueError("Digite o nome.")

            if not cpf:
                raise ValueError("Digite o CPF.")

            if not saldo_texto:
                raise ValueError("Digite o saldo inicial.")

            saldo = float(saldo_texto)

            if saldo < 0:
                raise ValueError(
                    "O saldo inicial não pode ser negativo."
                )

            cliente = Cliente(nome, cpf)
            conta = Conta(cliente, saldo)

            self.repository.salvar(conta)

            self.exibir_conta(conta)

            messagebox.showinfo(
                "Sucesso",
                "Conta criada e salva no arquivo TXT."
            )

        except ValueError as erro:
            messagebox.showerror(
                "Erro",
                str(erro)
            )

    def buscar_conta(self):
        cpf = self.cpf_entry.get().strip()

        if not cpf:
            messagebox.showerror(
                "Erro",
                "Digite o CPF da conta."
            )
            return

        conta = self.repository.buscar(cpf)

        if conta is None:
            messagebox.showerror(
                "Erro",
                "Conta não encontrada."
            )
            return

        self.exibir_conta(conta)

        messagebox.showinfo(
            "Conta encontrada",
            f"Conta de {conta.cliente.nome} encontrada com sucesso."
        )

    def depositar(self):
        try:
            cpf = self.cpf_entry.get().strip()
            valor_texto = self.valor_entry.get().strip()

            if not cpf:
                raise ValueError(
                    "Digite o CPF da conta."
                )

            if not valor_texto:
                raise ValueError(
                    "Digite o valor do depósito."
                )

            valor = float(valor_texto)

            conta = self.deposito_use_case.executar(
                cpf,
                valor
            )

            self.exibir_conta(conta)

            self.valor_entry.delete(
                0,
                tk.END
            )

            messagebox.showinfo(
                "Sucesso",
                "Depósito realizado com sucesso."
            )

        except ValueError as erro:
            messagebox.showerror(
                "Erro",
                str(erro)
            )

    def sacar(self):
        try:
            cpf = self.cpf_entry.get().strip()
            valor_texto = self.valor_entry.get().strip()

            if not cpf:
                raise ValueError(
                    "Digite o CPF da conta."
                )

            if not valor_texto:
                raise ValueError(
                    "Digite o valor do saque."
                )

            valor = float(valor_texto)

            conta = self.saque_use_case.executar(
                cpf,
                valor
            )

            self.exibir_conta(conta)

            self.valor_entry.delete(
                0,
                tk.END
            )

            messagebox.showinfo(
                "Sucesso",
                "Saque realizado com sucesso."
            )

        except ValueError as erro:
            messagebox.showerror(
                "Erro",
                str(erro)
            )

    def exibir_conta(self, conta):
        texto = (
            f"Conta ativa\n\n"
            f"Nome: {conta.cliente.nome}\n"
            f"CPF: {conta.cliente.cpf}\n"
            f"Saldo: R$ {conta.saldo:.2f}"
        )

        self.resultado.config(
            text=texto
        )