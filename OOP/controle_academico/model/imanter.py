from abc import ABC, abstractmethod

class IManter(ABC):

    @abstractmethod
    def adicionar(): ...

    @abstractmethod
    def pesquisar(): ...

    @abstractmethod
    def editar(): ...