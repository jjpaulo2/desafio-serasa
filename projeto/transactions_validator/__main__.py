"""
Arquivo de execução do módulo `transactions_validator`. Para executar este arquivo,
basta executar o seguinte comando:
    $ python -m transactions_validator

Loop que recebe json das transações via linha de comando e retorna o resuldado
da validação delas. Só para quando encontra EOF ou recebe Ctrl+C.
"""
import json, argparse
from . import validator

__command_line_description = """
Módulo que faz a verificação de uma transação de solicitação de crédito. A transação
deve ser inserida em um json seguindo o seguinte formato:
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

A forma recomendada de utilizar este programa é criando um arquivo de texto contendo
cada transação em uma linha, adotando o formato descrito acima. Contudo, também é possível
utilizar o programa apenas o executando direto e inserir manualmente o json da transação
no console.

Exemplo de uso:
    $ transations_validator < transacoes.txt

    {'transaction': {'id': 1, 'violations': ['low-score']}}
    {'transaction': {'id': 2, 'violations': ['minimum-installments']}}
    {'transaction': {'id': 3, 'violations': ['compromised-income']}}
    {'transaction': {'id': 4, 'success': 'Transação realizada com sucesso!'}}
    {'transaction': {'id': 5, 'success': 'Transação realizada com sucesso!'}}
    {'transaction': {'id': 6, 'success': 'Transação realizada com sucesso!'}}
    {'transaction': {'id': 7, 'violations': ['double-transactions']}}
"""


argparse.ArgumentParser(
    prog='transactions_validator',
    description=__command_line_description, 
    formatter_class=argparse.RawTextHelpFormatter
).parse_args()

while True:

    try:
        json_input: str = input()
        json_final = json.loads(json_input)

        validator_object = validator.Validator()
        result = validator_object.validateOne(json_final)

        print(result)

    except json.decoder.JSONDecodeError:
        print("O json deve estar formatado em aspas duplas.")

    except EOFError:
        break

    except KeyboardInterrupt:
        print()
        print("Programa encerrado pelo usuário.")
        break