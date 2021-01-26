import pytest

@pytest.fixture
def instructions_operations():
    return [
        { "transaction": { "id": 1, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 10000, "installments": 8, "time": "2019-02-13T10:00:00.000Z"}},
        { "transaction": { "id": 2, "consumer_id": 10, "score": 100, "income": 4000, "requested_value": 10000, "installments": 15, "time": "2019-03-13T10:00:00.000Z"}},
        { "transaction": { "id": 3, "consumer_id": 10, "score": 500, "income": 4000, "requested_value": 10000, "installments": 0, "time": "2019-04-13T10:00:00.000Z"}},
    ]

@pytest.fixture
def low_score():
    return [
        { "transaction": { "id": 1, "consumer_id": 10, "score": 150, "income": 4000, "requested_value": 10000, "installments": 15, "time": "2019-02-13T10:00:00.000Z"}},
        { "transaction": { "id": 2, "consumer_id": 10, "score": 100, "income": 4000, "requested_value": 10000, "installments": 15, "time": "2019-03-13T10:00:00.000Z"}},
        { "transaction": { "id": 3, "consumer_id": 10, "score": 200, "income": 4000, "requested_value": 10000, "installments": 0, "time": "2019-04-13T10:00:00.000Z"}},
    ]

@pytest.fixture
def minimum_installments():
    return [
        { "transaction": { "id": 1, "consumer_id": 10, "score": 400, "income": 4000, "requested_value": 10000, "installments": 2, "time": "2019-02-13T10:00:00.000Z"}},
        { "transaction": { "id": 2, "consumer_id": 10, "score": 400, "income": 4000, "requested_value": 10000, "installments": 4, "time": "2019-03-13T10:00:00.000Z"}},
        { "transaction": { "id": 3, "consumer_id": 10, "score": 400, "income": 4000, "requested_value": 10000, "installments": 0, "time": "2019-04-13T10:00:00.000Z"}},
    ]

@pytest.fixture
def compromised_income():
    return [
        { "transaction": { "id": 1, "consumer_id": 10, "score": 600, "income": 2000, "requested_value": 10000, "installments": 10, "time": "2019-02-13T10:00:00.000Z"}},
        { "transaction": { "id": 2, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 10000, "installments": 8, "time": "2019-02-13T10:00:00.000Z"}},
        { "transaction": { "id": 3, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 20000, "installments": 15, "time": "2019-02-13T10:00:00.000Z"}},
    ]

@pytest.fixture
def double_transactions():
    return [
        { "transaction": { "id": 1, "consumer_id": 10, "score": 150, "income": 4000, "requested_value": 10000, "installments": 15, "time": "2019-02-13T10:00:00.000Z"}},
        { "transaction": { "id": 2, "consumer_id": 10, "score": 150, "income": 4000, "requested_value": 12000, "installments": 10, "time": "2019-03-13T10:00:00.000Z"}},
        { "transaction": { "id": 3, "consumer_id": 10, "score": 150, "income": 4000, "requested_value": 10000, "installments": 15, "time": "2019-04-13T10:01:30.000Z"}},
    ]