def listar(lista):
    if len(lista) == 0:
        print('Não há o que listar')
        return 'vazia'
    for indice, item in enumerate(lista):
        print(indice, item)