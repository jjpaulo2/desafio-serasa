from typing import List

class TryingToParametrizeDataException(Exception):
    """
    Exceção invocada quando são passadas duas listas com
    tamanhos diferentes para a função `get_parametrized_data`.
    """
    def __init__(self):
        """
        Inicializador/construtor da exceção.
        """
        self.message = "Você tentou parametrizar duas listas com tamanhos diferentes para um teste."
        super().__init__(self.message)

def get_parametrized_data(input_values: List[dict], expected_return_values: List[dict]) -> List[tuple]:
    """
    Função que converte as listas de dados de entrada e saida para o formato
    lido pelo `@pytest.mark.parametrize()`.

    Arguments:
        input_values (List[dict]): Lista com transações
        expected_return_values (List[dict]): Lista com o resultado esperado ao validar a lista `input_values`

    Returns:
        List[tuple]: [(in1, out1), (in2, out2), ...]
    """
    size = len(input_values)

    if size == len(expected_return_values):
        return [(input_values[i], expected_return_values[i]) for i in range(size)]

    else:
        raise TryingToParametrizeDataException