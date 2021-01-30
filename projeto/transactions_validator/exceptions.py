class LowScoreException(Exception):
    """
    Exceção invocada quando o score passado na transação for inferior a 200.

    Atributos:
        id (int): Identificação da transação
        message (str): Mensagem exibida ao lançar a exceção
        json (dict): Dicionário para tratamento da exceção
    """

    def __init__(self, transaction_id: int):
        """
        Construtor/inicializador da exceção.
        """

        self.message = "O valor do score é menor que 200."
        self.json = { "transaction": { "id": transaction_id, "violatios": ["low-score"] }}

        super().__init__(self.message)


class CompromisedIncomeException(Exception):
    """
    Exceção invocada quando o valor das prestações ultrapassa 30% da renda.

    Atributos:
        id (int): Identificação da transação
        message (str): Mensagem exibida ao lançar a exceção
        json (dict): Dicionário para tratamento da exceção
    """

    def __init__(self, transaction_id: int):
        """
        Construtor/inicializador da exceção.
        """

        self.message = "O valor das prestações ultrapassa 30%% da renda."
        self.json = { "transaction": { "id": transaction_id, "violatios": ["compromised-income"] }}

        super().__init__(self.message)


class MinimumInstallmentsException(Exception):
    """
    Exceção invocada quando a quantidade de prestações for menor que 6.

    Atributos:
        id (int): Identificação da transação
        message (str): Mensagem exibida ao lançar a exceção
        json (dict): Dicionário para tratamento da exceção
    """

    def __init__(self, transaction_id: int):
        """
        Construtor/inicializador da exceção.
        """

        self.message = "A quantidade de prestações é menor que 6."
        self.json = { "transaction": { "id": transaction_id, "violatios": ["minimum-installments"] }}

        super().__init__(self.message)


class DoubleTransactionsException(Exception):
    """
    Exceção invocada quando a mesma transação tiver sido aprovada em menos de 2 minutos.

    Atributos:
        id (int): Identificação da transação
        message (str): Mensagem exibida ao lançar a exceção
        json (dict): Dicionário para tratamento da exceção
    """

    def __init__(self, transaction_id: int):
        """
        Construtor/inicializador da exceção.
        """

        self.message = "A mesma transação foi socilitada em menos de 2 minutos."
        self.json = { "transaction": { "id": transaction_id, "violatios": ["double-transactions"] }}

        super().__init__(self.message)