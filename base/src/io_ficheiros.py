import pickle
from clientes import nome_ficheiro_lista_de_clientes
from faturas import nome_ficheiro_lista_de_faturas
from veiculos import nome_ficheiro_lista_de_veiculos

def carrega_as_listas_dos_ficheiros():
    """
    Carrega as listas de veículos, clientes e faturas dos respectivos arquivos.

    :return: Uma tupla contendo as listas de veículos, clientes e faturas.
    :rtype: tuple
    """
    lista_de_veiculos = le_de_ficheiro(nome_ficheiro_lista_de_veiculos)
    lista_de_clientes = le_de_ficheiro(nome_ficheiro_lista_de_clientes)
    lista_de_faturas = le_de_ficheiro(nome_ficheiro_lista_de_faturas)

    return lista_de_veiculos, lista_de_clientes, lista_de_faturas

def guarda_as_listas_em_ficheiros(lista_de_veiculos, lista_de_clientes, lista_de_faturas):
    """
    Guarda as listas de veículos, clientes e faturas nos respetivos arquivos.

    :param lista_de_veiculos: Lista de veículos a ser guardada.
    :type lista_de_veiculos: list
    :param lista_de_clientes: Lista de clientes a ser guardada.
    :type lista_de_clientes: list
    :param lista_de_faturas: Lista de faturas a ser guardada.
    :type lista_de_faturas: list
    """
    op = input("Os dados nos ficheiros serão sobrepostos. Continuar (s/N)?")
    if op in ['s', 'S']:
        guarda_em_ficheiro(nome_ficheiro_lista_de_veiculos, lista_de_veiculos)
        guarda_em_ficheiro(nome_ficheiro_lista_de_clientes, lista_de_clientes)
        guarda_em_ficheiro(nome_ficheiro_lista_de_faturas, lista_de_faturas)
    else:
        print("Gravação cancelada...")

def guarda_em_ficheiro(nome_do_ficheiro, dados):
    """
    Guarda os dados no arquivo usando o módulo pickle.

    :param nome_do_ficheiro: Nome do arquivo onde os dados serão guardados.
    :type nome_do_ficheiro: str
    :param dados: Dados a serem guardados no arquivo.
    :type dados: any
    """
    with open(nome_do_ficheiro, "wb") as f:
        pickle.dump(dados, f)

def le_de_ficheiro(nome_ficheiro):
    """
    Lê os dados do arquivo usando o módulo pickle.

    :param nome_ficheiro: Nome do arquivo a ser lido.
    :type nome_ficheiro: str
    :return: Dados lidos do arquivo.
    :rtype: any
    """
    with open(nome_ficheiro, "rb") as f:
        return pickle.load(f)
