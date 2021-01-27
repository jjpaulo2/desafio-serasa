import abc
from typing import List

class FixtureClass(metaclass=abc.ABCMeta):
    """
    Classe que guarda casos de uso e resultados esperados para
    tratar uma exceção específica.
    """

    @abc.abstractstaticmethod
    def use_cases_exception() -> List[dict]:
        """
        Deve retornar casos de teste que invocam a exceção da classe.
        """
        raise NotImplementedError

    @abc.abstractstaticmethod
    def result_violation() -> List[dict]:
        """
        Deve retornar os valores esperados de retorno ao invocar a exceção.
        """
        raise NotImplementedError

    @abc.abstractstaticmethod
    def use_cases_no_exception() -> List[dict]:
        """
        Deve retornar casos de teste que não invocam a exceção da classe.
        """
        raise NotImplementedError

    @abc.abstractstaticmethod
    def result_success() -> List[dict]:
        """
        Deve retornar os valores esperados de retorno ao não invocar a exceção.
        """
        raise NotImplementedError