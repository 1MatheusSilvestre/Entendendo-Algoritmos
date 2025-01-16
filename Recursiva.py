#A recursão é quando um módulo faz uma chamada ou ativa a si mesmo
def procurar_chave(caixa_principal):
    for item in caixa:
        #olhar caixa
        if item.e_uma_caixa():
            #se achar outra caixa voltar passo 1
            procurar_chave(item)#RECURSAO
            #achou chave
        elif item.e_uma_chave():
            print('achei a chave!')


def regressiva(i):
    print(i)
    if i <= 1: #csao-base: quando n chama a si mesma novamente
        return
    else:
        regressiva(i-1) #caso-recursivo: quando chama si mesma 


def sauda(nome):
    print ('Olá, ' + nome + '!')
    sauda2(nome)
    print ('preparando para dizer tchau...')
    tchau()


def sauda2(nome):
    print ('como vai, ' + nome + '?')


def tchau():
    print ('tchau!')
