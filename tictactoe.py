#ist199333   Tiago Miguel Rocha dos Santos

def eh_tabuleiro(tab):
    """Retorna o valor booleano da proposicao 'argumento eh um tabuleiro valido?'."""
    if type(tab) == tuple and len(tab) == 3:
        for linha in tab:
            if type(linha) == tuple and len(linha) == 3:
                for i in linha:
                    if str(i) in ("-1", "0", "1") and type(i) == int: #se todos os valores nas linhas sao validos.
                        continue #continua-se o loop e, caso todos sejam validos, retorna True.
                    else:
                        return False
            else:
                return False
        return True #So retorna o valor booleano True quando verifica todas as condicoes.
    else:
        return False

def eh_posicao(n):
    """Retorna o valor booleano da proposicao 'argumento eh uma posicao valida?'."""
    return type(n) == int and n in range(1, 10) and str(n) != "True" #Retorna a conjuncao das condicoes necessarias para que n seja uma posicao valida.

def obter_coluna(tab, n):
    """Recebe um tabuleiro, tab, e um inteiro, n.
    Retorna o tuplo correspondente ah coluna de indice n-1 do tabuleiro"""
    if eh_tabuleiro(tab) and str(n) in ('1', '2', '3'):#Como o valor True pode ser lido como 1, tem de se verificar que a cc do inteiro e igual as CCs especificadas. O mesmo metodo e usado em outras funcoes.
        res = ()
        for i in range(3):
            res = res + (tab[i][n-1],) #Adiciona ao tuplo res os valores da coluna de indice n-1 do tabuleiro.
        return res
    else:
        raise ValueError("obter_coluna: algum dos argumentos e invalido")

def obter_linha(tab, n):
    """Recebe um tabuleiro, tab, e um inteiro, n.
    Retorna o tuplo correspondente ah linha de indice n-1 do tabuleiro"""
    if eh_tabuleiro(tab) and str(n) in ('1', '2', '3'):
        return tab[n-1] #Retorna a linha de indice n-1 do tabuleiro.
    else:
        raise ValueError("obter_linha: algum dos argumentos e invalido")

def obter_diagonal(tab, d):
    """Recebe um tableiro, tab, e um inteiro, d, que deve ser 1 ou 2.
    Retorna o tuplo que contem os valores na diagonal principal (esquerda para a direita, cima para baixo) do
    tabuleiro, para d = 1, e retorna o tuplo que contem os valores na diagonal oposta (esquerda para a direita, baixo
    para cima) do tabuleiro para d = 2"""
    if eh_tabuleiro(tab) and str(d) in ('1', '2'):
        diagonal = ()
        if d == 1:
            for i in range(3):
                diagonal = diagonal + (tab[i][i], )  #Adiciona ao tuplo diagonal o valor contido na posicao de indice i da linha de indice i do tabuleiro.
        else:
            while d >= 0:
                diagonal = diagonal + (tab[d][-d + 2],)  #Adiciona ao tuplo diagonal os valores de coordenadas (2, 0), (1, 1), (0, 2) do tabuleiro decrementando o valor d, sendo, sempre, d = 2, sendo a soma sempre igual a 2.
                d = d - 1
        return diagonal
    else:
        raise ValueError("obter_diagonal: algum dos argumentos e invalido")

def tabuleiro_str(tab):
    """Recebe um tabuleiro, tab.
    Retorna a cadeia de caracteres que, quando em argumento da
    funcao print, retorna uma representacao visual do tabuleiro de jogo."""
    if eh_tabuleiro(tab):
        str = ""
        j = 0
        a = 0
        for i in range(3):
            barra = "|"
            for value in tab[i]: #Para cada valor do tabuleiro, por ordem, por linha.
                if j == 2:     #
                    j = 0      #So se adiciona 2 barras por linha
                    barra = "" #
                else:
                    j = j + 1
                if value == 1:                #
                    str = str + " X " + barra #
                elif value == 0:              # Correspondencia entre os valores e
                    str = str + "   " + barra # a sua representacao visual.
                else:                         #
                    str = str + " O " + barra #
            if a != 2:                       #}
                str = str + "\n-----------\n"#}So se adiciona duas barras divisorias entre linhas
            a = a + 1                        #}
        return str
    else:
        raise ValueError("tabuleiro_str: o argumento e invalido")

def eh_posicao_livre(tab, n):
    """Recebe um tabuleiro, tab, e um inteiro, n.
    Retorna o valor booleano da proposicao 'n eh uma posicao livre do tabuleiro?'."""
    if eh_tabuleiro(tab) and eh_posicao(n):
        if n <= 3:                               #
            return obter_linha(tab, 1)[n-1] == 0 #
        if n <= 6:                               #Necessario sendo que, como len(tab, i) == 3, do eh_tabuleiro, (tab, i)[2 + k], k inteiro positivo, estah fora dos limites do tuplo.
            return obter_linha(tab, 2)[n-4] == 0 #
        else:                                    #
            return obter_linha(tab, 3)[n-7] == 0 #
    else:
        raise ValueError("eh_posicao_livre: algum dos argumentos e invalido")

def obter_posicoes_livres(tab):
    """Recebe um tabuleiro tab.
    Retorna o tuplo com todos os valores que quando argumentos da funcao eh_posicao_livre retornam o valor booleano 'True'."""
    if eh_tabuleiro(tab):
        pos = ()
        for a in range(1, 10):
            if eh_posicao_livre(tab, a): #Ciclo que verifica se cada uma das posicoes se encontra livre, adicionando, as livres, ao tuplo pos.
                pos = pos + (a, )
        return pos
    raise ValueError("obter_posicoes_livres: o argumento e invalido")

def jogador_ganhador(tab):
    """Recebe um tabuleiro tab.
    Retorna o valor do jogador que tem 3 figuras em linha, ou retorna 0 se nao existir nenhum jogador nestas condicoes."""
    if eh_tabuleiro(tab):
        for linha in tab:
            res = 0
            for i in range(3):
                res = res + linha[i]
                if abs(res) == 3:
                    return int(res/3) #Retorna -1 se a soma for -3, ou seja, se houver um tres em linha do jogador -1, semelhante para o jogador 1 e para as 2 outras situacoes abaixo.
        for i in range(1, 4):
            res = 0
            for j in range(3):
                res = res + obter_coluna(tab, i)[j]
                if abs(res) == 3:
                    return int(res / 3)
        for i in (1, 2):
            res = 0
            for j in range(3):
                res = res + obter_diagonal(tab, i)[j]
                if abs(res) == 3:
                    return int(res / 3)
        return 0 #Retorna 0 se nao houver jogador ganhador.
    raise ValueError("jogador_ganhador: o argumento e invalido")

def marcar_posicao(tab, j, n):
    """Recebe um tabuleiro, tab, um jogador, j, e uma posicao, n.
    Retorna o tabuleiro em tudo igual ao tabuleiro de entrada mas com a posicao n alterada para j."""
    if eh_tabuleiro(tab) and eh_posicao(n) and eh_posicao_livre(tab, n) and j in (-1, 1) and type(j) == int:
        newline = ()
        if n <= 3:                                     #
            n = n - 1                                  #
            for i in range(3):                         #
                if i == n:                             #Cria um tuplo com a linha que contem a posicao alterada.
                    newline = newline + (j,)           #
                else:                                  #
                    newline = newline + (tab[0][i], )  #
            return (newline, ) + (tab[1],) + (tab[2],) #Nesta linha, retorna o tabuleiro que contem duas das linhas originais do tabuleiro e a linha modificada, o mesmo ocorre para as duas outras situacoes abaixo.
        if n <= 6:
            n = n - 4
            for i in range(3):
                if i == n:
                    newline = newline + (j, )
                else:
                    newline = newline + (tab[1][i], )
            return (tab[0],) + (newline,) + (tab[2],)
        else:
            n = n - 7
            for i in range(3):
                if i == n:
                    newline = newline + (j, )
                else:
                    newline = newline + (tab[2][i], )
            return (tab[0],) + (tab[1],) + (newline,)
    raise ValueError("marcar_posicao: algum dos argumentos e invalido")

def escolher_posicao_manual(tab):
    """Recebe um tabuleiro, tab.
    Pede ao utilizador para inserir uma posicao e retorna-a caso esta esteja livre no tabuleiro."""
    if eh_tabuleiro(tab):
        n = int(input("Turno do jogador. Escolha uma posicao livre: ")) #Pede ao jogador humano uma posicao.
        if type(n) == int and n in range(1, 10):
            if eh_posicao_livre(tab, n):
                return n
            else:
                raise ValueError("escolher_posicao_manual: a posicao introduzida e invalida")
        else:
            raise ValueError("escolher_posicao_manual: a posicao introduzida e invalida")
    else:
        raise ValueError("escolher_posicao_manual: o argumento e invalido")

def bloqueio(tab, j):
    """Recebe um tabuleiro e um jogador.
    Retorna um tuplo contendo todas as posicoes em que o oponente deve jogar para ganhar ou retorna 0 caso estas nao existam."""
    return vitoria(tab, -j) #Retorna as posicoes de vitoria do oponente, posicoes nas quais o jogador deve jogar para bloquear o oponente.

def bifurcacao(tab, j):
    pos = ()
    for i in range(1, 10):
        if eh_posicao_livre(tab, i):
            tab1 = marcar_posicao(tab, j, i) #Cria um tabuleiro ficticio que contem uma posicao livre marcada.
            if type(vitoria(tab1, j)) == tuple and len(vitoria(tab1, j)) == 2: #Verifica se, para o tabuleiro modificado, o jogador possui duas posicoes de vitoria.
                pos = pos + (i,)
    if sum(pos) != 0:
        return pos
    else:
        return 0

def bloqueio_bifurcacao(tab, j):
    """Recebe um tabuleiro e um jogador.
    Retorna um tuplo com a posicao de bifurcacao do adversario, caso seja unica, ou
    retorna um tuplo contendo as posicoes em que o jogador deve jogar de modo a criar um 2 em linha
    desde que a defesa do adversario nao resulte na criacao de uma bifurcacao para o adversario."""
    if type(bifurcacao(tab, -j)) == tuple and len(bifurcacao(tab, -j)) == 1: #Se o oponente tem apenas uma bifurcacao, o jogador deve jogar nessa posicao de bifurcacao, bloqueando-a.
        return bifurcacao(tab, -j)
    else:
        pos = ()
        for i in (1, 2, 3):                                                            #
            if sum(obter_linha(tab, i)) == j and -j not in obter_linha(tab, i):        #
                for k in (0, 1, 2):                                                    #
                    if obter_linha(tab, i)[k] == 0:                                    #
                        pos = pos + ((i - 1) * 3 + k + 1,)                             #
            if sum(obter_coluna(tab, i)) == j and -j not in obter_coluna(tab, i):      #
                for k in (0, 1, 2):                                                    #
                    if obter_coluna(tab, i)[k] == 0:                                   #
                        pos = pos + (k * 3 + i,)                                       #Adiciona a um tuplo todas as posicoes que criam um dois em linha para o jogador.
        for i in (1, 2):                                                               #
            if sum(obter_diagonal(tab, i)) == j and -j not in obter_diagonal(tab, i):  #
                for k in (0, 1, 2):                                                    #
                    if obter_diagonal(tab, i)[k] == 0:                                 #
                        if i == 1:                                                     #
                            pos = pos + ((2 - k) * 3 + k + 1,)                         #
                        else:                                                          #
                            pos = pos + (k * 3 + k + 1,)                               #
        posfinal = ()
        if len(pos) != 0:                                                                        #
            for i in pos:                                                                        #
                if eh_posicao_livre(tab, i):                                                     #
                    tab1 = marcar_posicao(tab, j, i)                                             #Verifica se o bloqueio, por parte do adversario, do dois em linha do jogador, cria uma bifurcacao contra o jogador.
                    if type(bloqueio(tab1, -j)) == tuple and type(bifurcacao(tab, -j)) == tuple: #
                        for e in bloqueio(tab1, -j):                                             #
                            if e not in bifurcacao(tab, -j):                                     #
                                posfinal = posfinal + (i,)                                       #
        else:
            return 0
        return posfinal #Retorna as posicoes que criam um dois em linha e que verificam a condicao acima descrita.

def vitoria(tab, j):
    """Recebe um tabuleiro e um jogador.
    Retorna um tuplo com todas as posicoes em que o jogador deve jogar de modo a ganhar o jogo."""
    pos = ()
    for i in (1, 2, 3):                                    #
        if sum(obter_linha(tab, i)) == (2 * j):            #
            for k in (0, 1, 2):                            #
                if obter_linha(tab, i)[k] == 0:            #
                    pos = pos + (k + 1 + (i - 1) * 3,)     #
        if sum(obter_coluna(tab, i)) == (2 * j):           #
            for k in (0, 1, 2):                            #
                if obter_coluna(tab, i)[k] == 0:           #
                    pos = pos + ((k * 3) + i, )            #Verifica se existe um 2 em linha por parte do jogador e retorna a posicao vazia entre os dois em linha.
    for i in (1, 2):                                       #
        if sum(obter_diagonal(tab, i)) == 2 * j:           #
            for k in (0, 1, 2):                            #
                if obter_diagonal(tab, i)[k] == 0:         #
                    if i == 1:                             #
                        pos = pos + (k * 3 + k + 1,)       #
                    else:                                  #
                        pos = pos + ((2 - k) * 3 + k + 1,) #
    if sum(pos) != 0:
        posfinal = ()
        for e in pos:
            if eh_posicao_livre(tab, e):
                posfinal = posfinal + (e,) #Verifica se sao posicoes livres, caso o sejam, retorna o tuplo contendo-as.
        return posfinal
    return 0

def escolher_posicao_auto(tab, j , modo):
    """Recebe um tabuleiro, tab, um jogador, j, e um modo, ('basico', 'normal', 'perfeito').
    Retorna a posicao mais favoravel para o jogador j jogar, segundo um algoritmo de estrategia modificado pela cc modo."""
    if eh_tabuleiro(tab) and modo in ('basico', 'normal', 'perfeito') and j in (-1, 1) and type(j) == int:
        if modo == "basico": #Algoritmo no modo basico

            if eh_posicao_livre(tab, 5): #Verifica se o centro se encontra livre.
                return 5

            for i in (1, 3, 7, 9):       #Verifica se os cantos se encontram livres.
                if eh_posicao_livre(tab, i):
                    return i
            for i in (2, 4, 6, 8):       #Verifica se as laterais se encontram livres.
                if eh_posicao_livre(tab, i):
                    return i

        if modo == "normal":

            if vitoria(tab, j) != 0:      #Verifica se existem posicoes livres que criam um tres em linha para o jogador, retornando-as.
                return min(vitoria(tab, j))

            if bloqueio(tab, j) != 0:     #Verifica se existem posicoes livres que criam um tres em linha para o oponente, retornando-as.
                return min(bloqueio(tab, j))

            if eh_posicao_livre(tab, 5):
                return 5

            for i in (1, 2):                                                           #
                if obter_diagonal(tab, i)[0] == -j and obter_diagonal(tab, i)[2] == 0: #
                    if i == 1:                                                         #
                        if eh_posicao_livre(tab, 9):                                   #
                            return 9                                                   #
                    else:                                                              #
                        if eh_posicao_livre(tab, 3):                                   #
                            return 3                                                   #Verifica se o oponente se encontra num canto, retornando o canto oposto caso se verifique.
                if obter_diagonal(tab, i)[2] == -j and obter_diagonal(tab, i)[0] == 0: #
                    if i == 1:                                                         #
                        if eh_posicao_livre(tab, 1):                                   #
                            return 1                                                   #
                    else:                                                              #
                        if eh_posicao_livre(tab, 7):                                   #
                            return 7                                                   #

            for i in (1, 3, 7, 9):
                if eh_posicao_livre(tab, i):
                    return i

            for i in (2, 4, 6, 8):
                if eh_posicao_livre(tab, i):
                    return i

        if modo == "perfeito":
            if vitoria(tab, j) != 0:
                return min(vitoria(tab, j))

            if bloqueio(tab, j) != 0:
                return min(bloqueio(tab, j))

            if bifurcacao(tab, j) != 0: #Verifica se existem posicoes de bifurcacao para o jogador, retornando-as.
                return min(bifurcacao(tab, j))

            if bloqueio_bifurcacao(tab, j) != 0 and bloqueio_bifurcacao(tab, j) != (): #Verifica se existem posicoes de bloqueio de bifurcacao para o jogador, retornando-as.
                return min(bloqueio_bifurcacao(tab, j))

            if eh_posicao_livre(tab, 5):
                return 5

            for i in (1, 2):
                if obter_diagonal(tab, i)[0] == -j and obter_diagonal(tab, i)[2] == 0:
                    if i == 1:
                        if eh_posicao_livre(tab, 3):
                            return 3
                    else:
                        if eh_posicao_livre(tab, 9):
                            return 9
                if obter_diagonal(tab, i)[2] == -j and obter_diagonal(tab, i)[0] == 0:
                    if i == 1:
                        if eh_posicao_livre(tab, 1):
                            return 1
                    else:
                        if eh_posicao_livre(tab, 7):
                            return 7

            for i in (1, 3, 7, 9):
                if eh_posicao_livre(tab, i):
                    return i

            for i in (2, 4, 6, 8):
                if eh_posicao_livre(tab, i):
                    return i
    else:
        raise ValueError("escolher_posicao_auto: algum dos argumentos e invalido")


def jogo_do_galo(jogador, modo):
    """Funcao principal do programa, recebe um jogador, 'X' ou 'O', e um modo, 'basico', 'normal' ou 'perfeito'.
    Comeca o jogador com 'X'. O chamamento desta funcao inicia o jogo e implementa as funcoes necessarias para o correr."""
    if jogador in ('X', 'O') and modo in ('basico', 'normal', 'perfeito'):
        print('Bem-vindo ao JOGO DO GALO.\nO jogador joga com ' + "'" + jogador + "'.")
        tab = ((0, 0, 0), (0, 0, 0), (0, 0, 0))
        if jogador == "O":
            computador = "X"
            j = -1            #Atribui ao jogador humano o valor -1 caso este escolha a figura 'O'.
            pessoa = False    #Determina quem joga
        else:
            computador = "O"
            j = 1             #Atribui ao jogador humano o valor  1 caso este escolha a figura 'X'.
            pessoa = True
        ganhador = ""
        while jogador_ganhador(tab) == 0 and len(obter_posicoes_livres(tab)) != 0: #Enquanto nao houver um jogador ganhador e haja posicoes livres.
            if pessoa:
                pessoa = False                                                   #Se for o turno do jogador humano, pessoa = !pessoa, passando a vez para o computador.
                i = eval(input('Turno do jogador. Escolha uma posicao livre: ')) #Posicao escolhida pelo jogador humano.
                tab = marcar_posicao(tab, j, i)                                  #Modifica o tabuleiro, marcando uma posicao.
                print(tabuleiro_str(tab))                                        #Escreve uma representacao visual do tabuleiro no ecra.
                if jogador_ganhador(tab) == j:                                   #Se houver vencedor e for o jogador humano, declara-o na variavel 'ganhador'.
                    ganhador = jogador
            else:
                pessoa = True                                      #Se for o turno do jogador computador, pessoa = !pessoa, passando a vez para o humano.
                print('Turno do computador ' + '(' + modo + '):')
                i = escolher_posicao_auto(tab, -j, modo)           #Posicao escolhida pelo jogador computador.
                tab = marcar_posicao(tab, -j, i)                   #Modifica o tabuleiro, marcando uma posicao.
                print(tabuleiro_str(tab))                          #Escreve uma representacao visual do tabuleiro no ecra.
                if jogador_ganhador(tab) == -j:                    #Se houver vencedor e for o jogador computador, declara-o na variavel 'ganhador'.
                    ganhador = computador
            if ganhador == "":                                     #Se nao houver vencedor, declara que e um empate.
                ganhador = 'EMPATE'
        return ganhador
    else:
        raise ValueError("jogo_do_galo: algum dos argumentos e invalido")
