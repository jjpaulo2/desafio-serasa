from typing import List
from datetime import datetime, timedelta
from .exceptions import ( CompromisedIncomeException, 
                          DoubleTransactionsException, 
                          LowScoreException, 
                          MinimumInstallmentsException )

class Validator(object):
    """
    Classe que contém os métodos responsáveis por validar as transações 
    no formato `json/dict`. 

    Atributos:
        history (list): Pilha que guarda o histórico das transações processadas pela classe.

    Métodos:
        validateOne(transaction: dict) (dict)
        validateMany(transactions: List[dict]) (List[dict])
    """

    def __init__(self, starter_history: List[dict] = []):
        """
        Inicializador/construtor da classe.
        """
        self.__stack: List[dict] = starter_history

    # *
    # Histórico de transações
    # *

    @property
    def history(self):
        """
        Pilha do histórico de transações já processadas.
        """
        return self.__stack

    def __history_register(self, transaction: dict):
        """
        Método que registra transação no histórico.
        """
        self.__stack.append(transaction)


    # *
    # Funções que geram o json/dict que deve ser retornado ao fim da verificação.
    # *

    def __success_return_dict(self, transaction_id: int) -> dict:
        """
        Retorna o json/dict usado caso a verificação seja bem sucedida.

        Argumentos:
            transaction_id (int): identificador da transação

        Returns:
            dict
        """
        return { "transaction": { "id": transaction_id, "success": "Transação realizada com sucesso!" }}

    def __violation_return_dict(self, transaction_id: int, violation: str) -> dict:
        """
        Retorna o json/dict usado caso a verificação seja mal sucedida.

        Argumentos:
            transaction_id (int): identificador da transação

        Returns:
            dict
        """
        return { "transaction": { "id": transaction_id, "violations": [violation] }}


    # *
    # Funções responsáveis pelas etapas da validação.
    # *

    def verify_low_score(self, transaction_data: dict):
        """
        Método que faz a validação do score. Se o score for menor que 200,
        será lançada a exceção `LowScoreException`.

        Argumentos:
            transaction_data (dict): dados da transação em formato json/dict
        """
        if transaction_data['score'] < 200:
            raise LowScoreException(transaction_data['id'])

    def verify_compromised_income(self, transaction_data: dict):
        """
        Método que faz a validação da renda. Se o valor das parcelas superar
        30% da renda informada, será lançada a exceção `CompromisedIncomeException`.

        Argumentos:
            transaction_data (dict): dados da transação em formato json/dict
        """
        installments_value = transaction_data['requested_value'] / transaction_data['installments']
        income_percent = transaction_data['income'] * 0.3
        if installments_value > income_percent:
            raise CompromisedIncomeException(transaction_data['id'])

    def verify_minimum_installments(self, transaction_data: dict):
        """
        Método que faz a validação da quantidade de parcelas. Se a quantidade de
        parcelas for menor que 6, será lançada a exceção `MinimumInstallmentsException`.

        Argumentos:
            transaction_data (dict): dados da transação em formato json/dict
        """
        if transaction_data['installments'] < 6:
            raise MinimumInstallmentsException(transaction_data['id'])

    def verify_double_transactions(self, transaction_data: dict):
        """
        Método que verifica transações duplicadas. Se a mesma transação houver sido 
        solicidata em menos de 2 minutos, será lançada a exceção `DoubleTransactionsException`.

        Argumentos:
            transaction_data (dict): dados da transação em formato json/dict
        """
        for item in self.history:
            same = True

            for key in ['consumer_id', 'score', 'income', 'requested_value', 'installments']:
                item_key = item[key]
                transaction_key = transaction_data[key]
                if item_key != transaction_key:
                    same = False
                    break

            if same:
                time1 = datetime.strptime(item['time'], "%Y-%m-%dT%H:%M:%S.%fZ")
                time2 = datetime.strptime(transaction_data['time'], "%Y-%m-%dT%H:%M:%S.%fZ")
                variation = abs(time1 - time2)
                variation_seconds = variation.total_seconds()
                variation_hours = variation_seconds / 3600
                if variation_hours <= 2:
                    raise DoubleTransactionsException(transaction_data['id'])


    

    # *
    # Validação completa de transações
    # *

    def validateOne(self, transaction: dict):
        """
        Método que executa as funções de validação em uma única transação.
        """
        transaction_data = transaction['transaction']
        
        try:
            self.verify_low_score(transaction_data)
            self.verify_minimum_installments(transaction_data)
            self.verify_compromised_income(transaction_data)
            self.verify_double_transactions(transaction_data)
            
            json = self.__success_return_dict(transaction_data['id'])
        
        except LowScoreException:
            json = self.__violation_return_dict(transaction_data['id'], 'low-score')
        
        except MinimumInstallmentsException:
            json = self.__violation_return_dict(transaction_data['id'], 'minimum-installments')

        except CompromisedIncomeException:
            json = self.__violation_return_dict(transaction_data['id'], 'compromised-income')

        except DoubleTransactionsException:
            json = self.__violation_return_dict(transaction_data['id'], 'double-transactions')

        finally:
            self.__history_register(transaction_data)

        return json

    def validateMany(self, transactions: List[dict]):
        """
        Método que executa as funções de validação em uma lista de transações.
        """
        retorno = []
        for transaction in transactions:
            retorno.append(self.validateOne(transaction))

        return retorno