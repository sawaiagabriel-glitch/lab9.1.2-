from abc import ABC, abstractmethod


class IContaRepository(ABC):

    @abstractmethod
    def salvar(self, conta):
        pass

    @abstractmethod
    def buscar(self, cpf):
        pass

