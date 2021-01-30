"""
Arquivo de testes do módulo `transactions_validator` que contém os
testes de casos onde não é esperado o lançamento de exceções.
"""
import pytest
from transactions_validator import validator, exceptions
from tests.data.low_score_data import expected_no_exception_parametrize as low_score_data
from tests.data.compromised_income_data import expected_no_exception_parametrize as compromised_income_data
from tests.data.minimum_installments_data import expected_no_exception_parametrize as minimum_installments_data
from tests.data.double_transactions_data import expected_no_exception_parametrize as double_transactions_data

@pytest.mark.parametrize("transaction,expected_return", low_score_data)
def test_low_score(transaction, expected_return):
    """
    Método que testa os casos em que é esperada que a exceção
    `LowScoreException` não seja lançada.
    """
    validator_object = validator.Validator()
    raised = False

    try:
        transaction_data = transaction['transaction']
        validator_object.verify_low_score(transaction_data)

        returned = validator_object.validateOne(transaction)

    except exceptions.LowScoreException:
        raised = True

    assert returned == expected_return
    assert raised == False

@pytest.mark.parametrize("transaction,expected_return", compromised_income_data)
def test_compromised_income(transaction, expected_return):
    """
    Método que testa os casos em que é esperada que a exceção
    `CompromisedIncomeException` não seja lançada.
    """
    validator_object = validator.Validator()
    raised = False

    try:
        transaction_data = transaction['transaction']
        validator_object.verify_compromised_income(transaction_data)

        returned = validator_object.validateOne(transaction)

    except exceptions.CompromisedIncomeException:
        raised = True

    assert returned == expected_return
    assert raised == False


@pytest.mark.parametrize("transaction,expected_return", minimum_installments_data)
def test_minimum_installments(transaction, expected_return):
    """
    Método que testa os casos em que é esperada que a exceção
    `MinimumInstallmentsException` seja lançada.
    """
    validator_object = validator.Validator()
    raised = False

    try:
        transaction_data = transaction['transaction']
        validator_object.verify_minimum_installments(transaction_data)

        returned = validator_object.validateOne(transaction)

    except exceptions.MinimumInstallmentsException:
        raised = True

    assert returned == expected_return
    assert raised == False


@pytest.mark.parametrize("transaction,expected_return,starter_history", double_transactions_data)
def test_double_transactions(transaction, expected_return, starter_history):
    """
    Método que testa os casos em que é esperada que a exceção
    `DoubleTransactionsException` seja lançada.
    """
    validator_object = validator.Validator(starter_history=starter_history)
    raised = False

    try:
        transaction_data = transaction['transaction']
        validator_object.verify_double_transactions(transaction_data)

        returned = validator_object.validateOne(transaction)

    except exceptions.DoubleTransactionsException:
        raised = True

    assert returned == expected_return
    assert raised == False
