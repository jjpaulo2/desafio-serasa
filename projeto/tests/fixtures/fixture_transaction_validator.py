from .fixture_interface import FixtureClass
import pytest
from typing import List

class ChallengeFixtures(FixtureClass):
    """
    Classe com os tratamentos dos casos apresentados no documento de desafio.
    """

    @staticmethod
    @pytest.fixture
    def use_cases_exception() -> List[dict]:
        """
        Casos de uso propostos no início do documento que apresentou o desafio.
        """
        return [
            { "transaction": { "id": 1, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 10000, "installments": 8, "time": "2019-02-13T10:00:00.000Z"}},
            { "transaction": { "id": 2, "consumer_id": 10, "score": 100, "income": 4000, "requested_value": 10000, "installments": 15, "time": "2019-03-13T10:00:00.000Z"}},
            { "transaction": { "id": 3, "consumer_id": 10, "score": 500, "income": 4000, "requested_value": 10000, "installments": 0, "time": "2019-04-13T10:00:00.000Z"}},
        ]

    @property
    @staticmethod
    def result_violation() -> List[dict]:
        """
        Valores que devem ser retornados nos casos propostos no início do documento de desafio.
        """
        return [
            { "transaction": { "id": 1, "violations": ["compromised-income"] }},
            { "transaction": { "id": 2, "violations": ["low-score"] }},
            { "transaction": { "id": 3, "violations": ["minimum-installments"] }},
        ]


class LowScoreFixtures(FixtureClass):
    """
    Classe com os tratamentos da violação `low-score`, contendo os casos de uso 
    e retornos esperados ao lidar com a exceção `LowScoreException`.
    """
    
    @staticmethod
    @pytest.fixture
    def use_cases_exception() -> List[dict]:
        """
        Casos de uso que devem lançar a exceção `LowScoreException`.
        """
        return [
            { "transaction": { "id": 1, "consumer_id": 10, "score": 150, "income": 4000, "requested_value": 10000, "installments": 15, "time": "2019-02-13T10:00:00.000Z"}},
            { "transaction": { "id": 2, "consumer_id": 10, "score": 100, "income": 4000, "requested_value": 10000, "installments": 15, "time": "2019-03-13T10:00:00.000Z"}},
            { "transaction": { "id": 3, "consumer_id": 10, "score": 200, "income": 4000, "requested_value": 10000, "installments": 0, "time": "2019-04-13T10:00:00.000Z"}},
        ]

    @property
    @staticmethod
    def result_violation() -> List[dict]:
        """
        Valores que devem ser retornados quando for lançada a exceção `LowScoreException`.
        """
        return [
            { "transaction": { "id": 1, "violations": ["low-score"] }},
            { "transaction": { "id": 2, "violations": ["low-score"] }},
            { "transaction": { "id": 3, "violations": ["low-score"] }},
        ]

    @staticmethod
    @pytest.fixture
    def use_cases_no_exception() -> List[dict]:
        """
        Casos de uso que não devem lançar a exceção `LowScoreException`.
        """
        return [
            { "transaction": { "id": 1, "consumer_id": 10, "score": 400, "income": 4000, "requested_value": 10000, "installments": 15, "time": "2019-02-13T10:00:00.000Z"}},
            { "transaction": { "id": 2, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 10000, "installments": 15, "time": "2019-03-13T10:00:00.000Z"}},
            { "transaction": { "id": 3, "consumer_id": 10, "score": 900, "income": 4000, "requested_value": 10000, "installments": 15, "time": "2019-04-13T10:00:00.000Z"}},
        ]

    @property
    @staticmethod
    def result_success() -> List[dict]:
        """
        Valores que devem ser retornados quando não for lançada a exceção `LowScoreException`.
        """
        return [
            { "transaction": { "id": 1, "success": "Transação realizada com sucesso!" }},
            { "transaction": { "id": 2, "success": "Transação realizada com sucesso!" }},
            { "transaction": { "id": 3, "success": "Transação realizada com sucesso!" }},
        ]



class MinimumInstallmentsFixtures(FixtureClass):
    """
    Classe com os tratamentos da violação `minimum-installments`, contendo os casos de uso 
    e retornos esperados ao lidar com a exceção `MinimumInstallmentsException`.
    """

    @staticmethod
    @pytest.fixture
    def minimum_installments_exception() -> List[dict]:
        """
        Casos de uso que devem lançar a exceção `MinimumInstallmentsException`.
        """
        return [
            { "transaction": { "id": 1, "consumer_id": 10, "score": 400, "income": 4000, "requested_value": 10000, "installments": 2, "time": "2019-02-13T10:00:00.000Z"}},
            { "transaction": { "id": 2, "consumer_id": 10, "score": 400, "income": 4000, "requested_value": 10000, "installments": 4, "time": "2019-03-13T10:00:00.000Z"}},
            { "transaction": { "id": 3, "consumer_id": 10, "score": 400, "income": 4000, "requested_value": 10000, "installments": 0, "time": "2019-04-13T10:00:00.000Z"}},
        ]

    @property
    @staticmethod
    def minimum_installments_result_violation() -> List[dict]:
        """
        Valores que devem ser retornados quando for lançada a exceção `MinimumInstallmentsException`.
        """
        return [
            { "transaction": { "id": 1, "violations": ["minimum-installments"] }},
            { "transaction": { "id": 2, "violations": ["minimum-installments"] }},
            { "transaction": { "id": 3, "violations": ["minimum-installments"] }},
        ]

    @staticmethod
    @pytest.fixture
    def minimum_installments_no_exception() -> List[dict]:
        """
        Casos de uso que não devem lançar a exceção `MinimumInstallmentsException`.
        """
        return [
            { "transaction": { "id": 1, "consumer_id": 10, "score": 400, "income": 4000, "requested_value": 10000, "installments": 10, "time": "2019-02-13T10:00:00.000Z"}},
            { "transaction": { "id": 2, "consumer_id": 10, "score": 400, "income": 4000, "requested_value": 10000, "installments": 6, "time": "2019-03-13T10:00:00.000Z"}},
            { "transaction": { "id": 3, "consumer_id": 10, "score": 400, "income": 4000, "requested_value": 10000, "installments": 15, "time": "2019-04-13T10:00:00.000Z"}},
        ]

    @property
    @staticmethod
    def minimum_installments_result_success() -> List[dict]:
        """
        Valores que devem ser retornados quando não for lançada a exceção `MinimumInstallmentsException`.
        """
        return [
            { "transaction": { "id": 1, "success": "Transação realizada com sucesso!" }},
            { "transaction": { "id": 2, "success": "Transação realizada com sucesso!" }},
            { "transaction": { "id": 3, "success": "Transação realizada com sucesso!" }},
        ]



class CompromisedIncomeFixtures(FixtureClass):
    """
    Classe com os tratamentos da violação `compromised-income`, contendo os casos de uso 
    e retornos esperados ao lidar com a exceção `CompromisedIncomeException`.
    """

    @staticmethod
    @pytest.fixture
    def compromised_income_exception() -> List[dict]:
        """
        Casos de uso que devem lançar a exceção `CompromisedIncomeException`.
        """
        return [
            { "transaction": { "id": 1, "consumer_id": 10, "score": 600, "income": 2000, "requested_value": 10000, "installments": 10, "time": "2019-02-13T10:00:00.000Z"}},
            { "transaction": { "id": 2, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 10000, "installments": 8, "time": "2019-02-13T10:00:00.000Z"}},
            { "transaction": { "id": 3, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 20000, "installments": 15, "time": "2019-02-13T10:00:00.000Z"}},
        ]

    @property
    @staticmethod
    def compromised_income_result_violation() -> List[dict]:
        """
        Valores que devem ser retornados quando for lançada a exceção `CompromisedIncomeException`.
        """
        return [
            { "transaction": { "id": 1, "violations": ["compromised-income"] }},
            { "transaction": { "id": 2, "violations": ["compromised-income"] }},
            { "transaction": { "id": 3, "violations": ["compromised-income"] }},
        ]

    @staticmethod
    @pytest.fixture
    def compromised_income_no_exception() -> List[dict]:
        """
        Casos de uso que não devem lançar a exceção `CompromisedIncomeException`.
        """
        return [
            { "transaction": { "id": 1, "consumer_id": 10, "score": 600, "income": 2000, "requested_value": 5000, "installments": 10, "time": "2019-02-13T10:00:00.000Z"}},
            { "transaction": { "id": 2, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 7000, "installments": 8, "time": "2019-02-13T10:00:00.000Z"}},
            { "transaction": { "id": 3, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 1000, "installments": 15, "time": "2019-02-13T10:00:00.000Z"}},
        ]

    @property
    @staticmethod
    def compromised_income_result_success() -> List[dict]:
        """
        Valores que devem ser retornados quando não for lançada a exceção `CompromisedIncomeException`.
        """
        return [
            { "transaction": { "id": 1, "success": "Transação realizada com sucesso!" }},
            { "transaction": { "id": 2, "success": "Transação realizada com sucesso!" }},
            { "transaction": { "id": 3, "success": "Transação realizada com sucesso!" }},
        ]



class DoubleTransactionsFixtures(FixtureClass):
    """
    Classe com os tratamentos da violação `double-transactions`, contendo os casos de uso 
    e retornos esperados ao lidar com a exceção `DoubleTransactionsException`.
    """

    @staticmethod
    @pytest.fixture
    def double_transactions_exception() -> List[dict]:
        """
        Casos de uso que devem lançar a exceção `DoubleTransactionsException`.
        """
        return [
            { "transaction": { "id": 1, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 10000, "installments": 15, "time": "2019-02-13T10:00:00.000Z"}},
            { "transaction": { "id": 2, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 12000, "installments": 10, "time": "2019-03-13T10:00:00.000Z"}},
            { "transaction": { "id": 3, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 10000, "installments": 15, "time": "2019-04-13T10:01:30.000Z"}},
        ]

    @property
    @staticmethod
    def double_transactions_result_violation():
        """
        Valores que devem ser retornados quando for lançada a exceção `DoubleTransactionsException`.
        """
        return [
            { "transaction": { "id": 1, "success": "Transação realizada com sucesso!" }},
            { "transaction": { "id": 2, "success": "Transação realizada com sucesso!" }},
            { "transaction": { "id": 3, "violations": ["double-transactions"] }},
        ]

    @staticmethod
    @pytest.fixture
    def double_transactions_no_exception() -> List[dict]:
        """
        Casos de uso que não devem lançar a exceção `DoubleTransactionsException`.
        """
        return [
            { "transaction": { "id": 1, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 5000, "installments": 15, "time": "2019-02-13T10:00:00.000Z"}},
            { "transaction": { "id": 2, "consumer_id": 5, "score": 400, "income": 5000, "requested_value": 10000, "installments": 10, "time": "2019-03-13T10:00:00.000Z"}},
            { "transaction": { "id": 3, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 5000, "installments": 15, "time": "2019-04-13T10:01:30.000Z"}},
        ]

    @property
    @staticmethod
    def double_transactions_result_success() -> List[dict]:
        """
        Valores que devem ser retornados quando não for lançada a exceção `DoubleTransactionsException`.
        """
        return [
            { "transaction": { "id": 1, "success": "Transação realizada com sucesso!" }},
            { "transaction": { "id": 2, "success": "Transação realizada com sucesso!" }},
            { "transaction": { "id": 3, "success": "Transação realizada com sucesso!" }},
        ]
