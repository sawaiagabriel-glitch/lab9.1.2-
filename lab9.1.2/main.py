import tkinter as tk

from infrastructure.arquivo_conta_repository import ArquivoContaRepository
from application.use_cases.realizar_deposito import RealizarDepositoUseCase
from application.use_cases.realizar_saque import RealizarSaqueUseCase
from presentation.conta_view import ContaView


repository = ArquivoContaRepository("contas.txt")

deposito_use_case = RealizarDepositoUseCase(repository)
saque_use_case = RealizarSaqueUseCase(repository)

root = tk.Tk()

view = ContaView(
    root,
    repository,
    deposito_use_case,
    saque_use_case
)

root.mainloop()