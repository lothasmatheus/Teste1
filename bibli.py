r = "S"

while r == "S":  # enquanto a respota for sim, o programa vai continuar rodando

    nome = str(input("Nome: "))
    endereco = str(input("Endereço: "))
    pedido = str(input("Pedido: "))
    quantidade = int(input("Quantidade: "))
    print("Nome: {}\n  Endereço: {}\n Pedido: {}\n Quantidade: {}\n".format(nome, endereco, pedido, quantidade))
    r = str(input("Deseja cadastrar mais algum pedido? [S/N] \n\n")).upper()

import os  # função para limpar a tela e mostrar apenas a lista de clientes que fizeram o pedido

os.system("cls")
