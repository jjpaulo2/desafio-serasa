"""
Arquivo que contém os casos de uso (valores de entrada) e retornos esperados para
o tratamento da exceção `LowScoreException`.

Variáveis do arquivo:
    _starter_history(List[dict]): Histórico inicial da pilha de transações

    _use_cases_exception (List[dict]): Casos de uso que devem lançar exceção
    _use_cases_no_exception (List[dict]): Casos de uso que não devem lançar exceção

    _expected_result_violation (List[dict]): Retorno esperado ao lançar exceção
    _expected_result_success (List[dict]): Retorno esperado ao não lançar exceção

Variáveis públicas:
    expected_exception_parametrize (List[tuple]): Lista de tuplas do tipo (entrada, saída_esperada) que deve ser passada como parâmetro no teste de exceção esperada
    expected_no_exception_parametrize (List[tuple]): Lista de tuplas do tipo (entrada, saída_esperada) que deve ser passada como parâmetro no teste de exceção não esperada
"""

from typing import List
from . import get_parametrized_data

# *
# Variáveis do arquivo
# *

# Histórico inicial que deve ser usado para comparar com transações que serão feitas.
_starter_history: List[dict] = [
    { "id": 1, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 10000, "installments": 15, "time": "2019-02-13T10:00:00.000Z"},
    { "id": 2, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 12000, "installments": 10, "time": "2019-03-13T10:00:00.000Z"},
    { "id": 3, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 10000, "installments": 15, "time": "2019-04-13T10:01:30.000Z"},
]

# Casos de uso que devem lançar um `LowScoreException`
_use_cases_exception: List[dict] = [
    { "transaction": { "id": 1, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 10000, "installments": 15, "time": "2019-02-13T10:00:00.000Z"}},
    { "transaction": { "id": 2, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 12000, "installments": 10, "time": "2019-03-13T10:00:00.000Z"}},
    { "transaction": { "id": 3, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 10000, "installments": 15, "time": "2019-04-13T10:01:30.000Z"}},
]

# Casos de uso que não devem lançar exceção
_use_cases_no_exception: List[dict] = [
    { "transaction": { "id": 1, "consumer_id": 8, "score": 600, "income": 4000, "requested_value": 5000, "installments": 15, "time": "2019-02-13T10:00:00.000Z"}},
    { "transaction": { "id": 2, "consumer_id": 5, "score": 400, "income": 5000, "requested_value": 10000, "installments": 10, "time": "2019-03-13T10:00:00.000Z"}},
    { "transaction": { "id": 3, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 10000, "installments": 15, "time": "2019-04-13T12:02:30.000Z"}},
]

# Retorno esperado ao lançar exceção
_expected_result_violation: List[dict] = [
    { "transaction": { "id": 1, "violations": ["double-transactions"] }},
    { "transaction": { "id": 2, "violations": ["double-transactions"] }},
    { "transaction": { "id": 3, "violations": ["double-transactions"] }},
]

# Retorno esperado ao não lançar exceção
_expected_result_success: List[dict] = [
    { "transaction": { "id": 1, "success": "Transação realizada com sucesso!" }},
    { "transaction": { "id": 2, "success": "Transação realizada com sucesso!" }},
    { "transaction": { "id": 3, "success": "Transação realizada com sucesso!" }},
]


# *
# Variáveis públicas
# *

# Lista de tuplas do tipo (entrada, saída_esperada) que deve ser passada como parâmetro no teste de exceção esperada
expected_exception_parametrize: List[tuple] = get_parametrized_data(_use_cases_exception, _expected_result_violation, starter_history=_starter_history)

# Lista de tuplas do tipo (entrada, saída_esperada) que deve ser passada como parâmetro no teste de exceção não esperada
expected_no_exception_parametrize: List[tuple] = get_parametrized_data(_use_cases_no_exception, _expected_result_success, starter_history=_starter_history)
