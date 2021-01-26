import pytest, unittest
from transactions_validator import validator, exceptions
from tests.fixtures.fixture_transaction_validator import *

class TestTransactionsValidator(unittest.TestCase):
    """
    Class de testes do módulo `transactions_validator`. Esta classe
    deve conter os seguintes testes:
    * testes da classe Validator que lançam exceções
    * testes da classe Validator que não lançam exceções
    * testes da saída em json/string com erros
    * testes de saída em json/string sem erros
    """

    def setUp(self):
        """
        Configuração inicial antes da execução dos testes.
        """

        self.validator = validator.Validator()

    def test_low_score(self):
        """
        Método que testa os casos em que é esperada que a exceção
        `LowScoreException` seja lançada.
        """

        with pytest.raises(exceptions.LowScoreException):
            self.validator.validateMany(low_score)

    def test_compromised_income(self):
        """
        Método que testa os casos em que é esperada que a exceção
        `CompromisedIncomeException` seja lançada.
        """

        with pytest.raises(exceptions.CompromisedIncomeException):
            self.validator.validateMany(compromised_income)

    def test_minimum_installments(self):
        """
        Método que testa os casos em que é esperada que a exceção
        `MinimumInstallmentsException` seja lançada.
        """

        with pytest.raises(exceptions.MinimumInstallmentsException):
            self.validator.validateMany(minimum_installments)

    def test_double_transactions(self):
        """
        Método que testa os casos em que é esperada que a exceção
        `DoubleTransactionsException` seja lançada.
        """

        with pytest.raises(exceptions.DoubleTransactionsException):
            self.validator.validateMany(double_transactions)