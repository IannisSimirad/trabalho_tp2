from datetime import date
from io_terminal import imprime_lista, pergunta_id

nome_ficheiro_lista_de_faturas = "lista_de_faturas.pk"

def cria_nova_fatura(lista_de_clientes, lista_de_veiculos):
    """
    Pede ao utilizador para introduzir os dados de uma nova fatura.

    :param lista_de_clientes: Lista de clientes disponíveis.
    :type lista_de_clientes: list
    :param lista_de_veiculos: Lista de veículos disponíveis.
    :type lista_de_veiculos: list
    :return: Um dicionário com os dados da nova fatura,
             {"cliente": <<id_cliente>>, "veiculo": <<id_veiculo>>, "data": <<data>>, ...}
    :rtype: dict
    """
    id_cliente = pergunta_id(questao="Qual o id do cliente?", lista=lista_de_clientes, mostra_lista=True)
    id_veiculo = pergunta_id(questao="Qual o id do veiculo?", lista=lista_de_veiculos, mostra_lista=True)

    fatura = {
        "cliente": id_cliente,
        "veiculo": id_veiculo,
        "data": date.today()
    }

    return fatura

def imprime_lista_de_faturas(lista_de_faturas):
    """
    Imprime a lista de faturas.

    :param lista_de_faturas: Lista de faturas a ser impressa.
    :type lista_de_faturas: list
    """
    # TODO: Adicionar detalhes sobre o formato da lista_de_faturas
    # e como a função imprime_lista pode ser usada aqui.
    pass




