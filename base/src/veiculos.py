from io_terminal import imprime_lista

nome_ficheiro_lista_de_veiculos = "lista_de_veiculos.pk"

def cria_novo_veiculo():


    marca = input("marca? ")
    matricula = input("matricula? ").upper()
    

    veiculo = {"marca": marca,
               "matricula": matricula}

    return veiculo

def imprime_lista_de_veiculos(lista_de_veiculos):
   

    imprime_lista(cabecalho="Lista de Veiculos", lista=lista_de_veiculos)
