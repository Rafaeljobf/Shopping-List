def apagar_item(lista):
    for indice, item in enumerate(lista):
        print(indice, item)
        if len(lista) == 0:
            print('Não há o que apagar.')
            return 'erro'
    apagar_item = input('Digite o índice do que deseja apagar: ')
    if apagar_item.isdigit() == False:
        print('Digite apenas o número do índice.')
        return 'erro'
    apagar_item_int = int(apagar_item)
    if apagar_item_int >= len(lista):
        print('Índice inválido.')
    else:
        del lista[apagar_item_int]
        return 0