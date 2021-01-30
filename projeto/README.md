# Desafio do Serasa Experian

Neste projeto você vai encontrar os seguintes módulos:

- [`transactions_validator`](./transactions_validator)
- [`tests`](./tests)
- [`docs`](./docs)

## Dependências

As dependências do projeto estão gerenciadas via **Pipenv**, que permite a utilização de ambiente virtuais de forma mais cômoda. Então, primeiramente garanta que você tenha ele instalado em sua máquina.

```shell
$ pip install -U pipenv
```

Com o **Pipenv** instalado, instale as dependências do projeto e acesse o ambiente virtual com as dependências.

```shell
$ pipenv install
...
Installing dependencies from Pipfile.lock
...

$ pipenv shell
(projeto-v-BZcsMM) $
```

### Testes

Existe uma bateria de testes escrita com o auxílio da biblioteca **Pytest**. Você pode executá-los utilizando o seguinte comando.

```shell
(projeto-v-BZcsMM) $ pytest
```
    ============================= test session starts ==============================
    platform linux -- Python 3.8.6, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
    rootdir: /home/jjpaulo2/dev/python/teste-serasa/projeto
    collected 24 items                                                             

    tests/test_transactions_validator_exception_expected.py ............     [ 50%]
    tests/test_transactions_validator_exception_not_expected.py ............ [100%]

    ============================== 24 passed in 0.10s ==============================

### Documentação

Também existe uma ***autodoc*** gerada com o auxílio da biblioteca **Sphinx**. Em [`docs/build/html`](./docs/html) você deve encontrar esta documentação. Ela apenas exibe os conteúdo das ***docstrings*** dos módulos, classes e funções.

Para compilar o conteúdo da documentação, apenas digite o seguinte comando.

```shell
(projeto-v-BZcsMM) $ make html
```

## Exemplo de uso

O módulo [`transactions_validator`](./transactions_validator) pode ser facilmente utilizado como cliente de linha de comando.

```shell
(projeto-v-BZcsMM) $ python -m transactions_validator --help
```

    usage: transactions_validator [-h]

    Módulo que faz a verificação de uma transação de solicitação de crédito. 
    A transação deve ser inserida em um json seguindo o seguinte formato:
        { 
            "transaction": {
                "id": int, 
                "consumer_id": int, 
                "score": int, 
                "income": int, 
                "requested_value": int, 
                "installments": int, 
                "time": datetime
            }
        }

    A transação será aprovada se obedecer as seguintes regras:
        - score maior que 200
        - quantidade de parcelas maior que 6
        - valor das parcelas não pode ultrapassar 30% da renda
        - não tiver sido aprovada em menos de 2 minutos atrás

    A forma recomendada de utilizar este programa é criando um arquivo de texto
    contendo cada transação em uma linha, adotando o formato descrito acima.
    Contudo, também é possível utilizar o programa apenas o executando direto e
    inserir manualmente o json da transação no console.

    [...]

    optional arguments:
    -h, --help  show this help message and exit

Você pode utilizar a ferramenta de duas formas: 

1) Executando o módulo sem parâmetros e inserindo o json na mão. Desta forma, você pode continuar inserindo documentos, até encerrar o programa com o auxílio do comando `Ctrl+C`.

```shell
# EXEMPLO DO PRIMEIRO USO

>>> (projeto-v-BZcsMM) $ python -m transactions_validator

# Json inserido manualmente no console
>>> { "transaction": { "id": 1, "consumer_id": 10, "score": 150, "income": 4000, "requested_value": 10000, "installments": 15, "time": "2019-02-13T10:00:00.000Z"}} 

# Retorno da ferramenta
<<< {'transaction': {'id': 1, 'violations': ['low-score']}} 

# Usuário pressiona Ctrl+C
>>> ^C
<<< Programa encerrado pelo usuário.
```

2) Criando um arquivo de texto com um json por linha e passando ele para o comando. 
   
Conteúdo do arquivo [`transacoes.txt`](./transacoes.txt):
```
{ "transaction": { "id": 1, "consumer_id": 10, "score": 150, "income": 4000, "requested_value": 10000, "installments": 15, "time": "2019-02-13T10:00:00.000Z"}}
{ "transaction": { "id": 2, "consumer_id": 10, "score": 400, "income": 4000, "requested_value": 10000, "installments": 2, "time": "2019-02-13T10:00:00.000Z"}}
{ "transaction": { "id": 3, "consumer_id": 10, "score": 600, "income": 2000, "requested_value": 10000, "installments": 10, "time": "2019-02-13T10:00:00.000Z"}}
{ "transaction": { "id": 4, "consumer_id": 10, "score": 400, "income": 4000, "requested_value": 10000, "installments": 15, "time": "2019-02-13T10:00:00.000Z"}}
{ "transaction": { "id": 5, "consumer_id": 10, "score": 400, "income": 4000, "requested_value": 5000, "installments": 6, "time": "2019-03-13T10:00:00.000Z"}}
{ "transaction": { "id": 6, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 7000, "installments": 8, "time": "2019-02-13T10:00:00.000Z"}}
{ "transaction": { "id": 7, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 7000, "installments": 8, "time": "2019-02-13T10:00:00.000Z"}}
```

Passando o arquivo para o módulo:

```shell
(projeto-v-BZcsMM) $ python -m transactions_validator < transacoes.txt
```

Retorno do programa:

```
{'transaction': {'id': 1, 'violations': ['low-score']}}
{'transaction': {'id': 2, 'violations': ['minimum-installments']}}
{'transaction': {'id': 3, 'violations': ['compromised-income']}}
{'transaction': {'id': 4, 'success': 'Transação realizada com sucesso!'}}
{'transaction': {'id': 5, 'success': 'Transação realizada com sucesso!'}}
{'transaction': {'id': 6, 'success': 'Transação realizada com sucesso!'}}
{'transaction': {'id': 7, 'violations': ['double-transactions']}}
```