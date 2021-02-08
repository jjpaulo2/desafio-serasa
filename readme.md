# Python coding challenge

Este repositório contém o código fonte da minha solução para o desafio proposto na etapa prática de um processo seletivo para o cargo de **Desenvolvedor Python**.

O objetivo é receber um json com os dados de uma transação financeira e dizer se ela foi aprovada ou não, de acordo com as regras definidas.

## Instruções do desafio

Exibindo o conteúdo do arquivo que contém as transações.

```shell
$ cat operacoes.txt
```

    { "transaction": { "id": 1, "consumer_id": 10, "score": 600, "income": 4000, "requested_value": 10000, "installments": 15, "time": "2019-02-13T10:00:00.000Z"}}
    { "transaction": { "id": 2, "consumer_id": 10, "score": 100, "income": 4000, "requested_value": 10000, "installments": 15, "time": "2019-03-13T10:00:00.000Z"}}
    { "transaction": { "id": 3, "consumer_id": 10, "score": 500, "income": 4000, "requested_value": 10000, "installments": 0, "time": "2019-04-13T10:00:00.000Z"}}

Passando o arquivo para o módulo que faz a validação das transações.

```shell
$ validador < operacoes.txt
```

    { "transaction": { "id": 1, "violatios": ["compromised-income"] }}
    { "transaction": { "id": 2, "violatios": ["low-score"] }}
    { "transaction": { "id": 3, "violatios": ["minimum-installments"] }}

### Lógica

A saída deve indicar **`id da transação` + `violação de lógica de negócios`**.

| Nome da violação | Descrição |
|-|-|
| `low-score` | Valor do **score** menor que 200 |
| `compromised-income` | Valor das **parcelas** maior que 30% da **renda** |
| `minimum-installments` | Quantidade de **parcelas** menor que 6 |
| `doubled-transactions` | Duas transações iguais em menos de 2 minutos |

## Sobre o projeto

Dentre as `features` do projeto, posso citar:

- gerenciamento das dependências via **Pipenv**
- bateria de **testes unitários** escrito com a ajuda da biblioteca **Pytest**
- **documentação em html** dos módulos, classes e funções gerada com **Sphinx**
- estrutura dos commits utilizando **Git Flow** com track de **issues**
- módulo utilizável via **linha de comando**, com mensagem de ajuda ao passar flag `--help`

Lembre-se que para executar as instruções do projeto, você deve estar dentro do diretório `projeto`.

```shell
$ cd projeto
```

[Clique aqui](./projeto) para ver as instruções de instalação, testes e execução do projeto.

---
Made with :heart: by [@jjpaulo2](https://github.com/jjpaulo2)