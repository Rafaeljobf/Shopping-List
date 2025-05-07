import os

from list_package import input_usuario, add_lista, listar, apagar_item

indices_permitidos = ['i', 'a', 'l', 's']
lista_compras = []

while True:
    print('Selecione uma opção:')
    acao = input('[i]nserir [a]pagar [l]istar [s]air: ')     # Pergunta ao usuário a ação

    verificação = input_usuario(acao, indices_permitidos)
    if verificação == 'erro':
        continue                    # Volta à pergunta em caso de indice inválido

    if acao == 'i':        
        os.system('cls')
        add_lista(lista_compras)            # Acrescentar itens à lista

    if acao == 'l':     # Listar
        os.system('cls')
        listagem = listar(lista_compras)
        if listagem == 'vazia':
            continue
        
    if acao == 'a':                             # Apagar itens da lista
        apagar = apagar_item(lista_compras)
        if apagar == 'erro':
            continue

    if acao == 's':                     # Sair do laço
        break