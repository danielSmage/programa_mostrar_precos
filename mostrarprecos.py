# programa_mostrar_precos
#Uma base que pode ser modificada pra mostrar oque quiser ao usuário
def menu():
    print('======Bem vindo ao Programa======')
    print('A. Xerox')
    print('B. Digitalização')
    print('C. Envio')
    print('D. Exit')


a = 'xerox'
b = 'digitalização'
c = 'envio'

def programa(op):

    if (x == 'd'):
        print('Programa finalizado')
        return False

    elif (x == 'a'):
            print('R$ 0,30')

    elif (x == 'b'):
            print('R$ 1,00')

    elif (x == 'c'):
            print('R$ 2,00')
    else:
        print('Comando Inválido')
        return False
    return True

i = True
while i == True:
    menu()
    x = input('Digite uma resposta: ')
    x.lower()
    i = programa(x)
    if i == True:
        p = input('Deseja rodar o programa novamente? Y/N: ')
        p.lower()
        if p != 'y':
            i = False
