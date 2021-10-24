#ist199333 Tiago Santos

#TAD posicao
#Representacao interna:lista de 2 elementos(strings) (linha e coluna da posicao)
# cria_posicao: str x str --> posicao
# cria_copia_peca: posicao --> posicao
# obter_pos_c: posicao --> str
# obter_pos_l: posicao --> str
# eh_posicao: universal --> booleano
# posicoes_iguais: posicao x posicao --> booleano
# posicao_para_str: posicao --> str
# tipo_posicao: posicao --> str
# ordena_posicoes: tuplo --> tuplo
# obter_posicoes_adjacentes: posicao --> tuplo

def cria_posicao(c, l):
    '''cria_posicao: str x str --> posicao.
    Funcao construtora do TAD posicao.
    Recebe, na forma de cadeia de caracteres, uma
    coluna e uma linha e devolve a peca correspondente.
    '''
    if c in ('a', 'b', 'c') and l in ('1', '2', '3'):
        return [c, l]
    else:
        raise ValueError('cria_posicao: argumentos invalidos')


def cria_copia_posicao(p):
    '''cria_copia_posicao: posicao --> posicao.
    Funcao construtora do TAD posicao.
    Recebe uma posicao e devolve uma copia dessa posicao.
    '''
    if eh_posicao(p):
        return cria_posicao(obter_pos_c(p), obter_pos_l(p))
    raise ValueError('cria_copia_posicao: argumentos invalidos')


def obter_pos_c(p):
    '''obter_pos_c: posicao --> str.
    Funcao seletora do TAD posicao.
    Recebe uma posicao e retorna a coluna que essa posicao ocupa.
    '''
    return p[0]


def obter_pos_l(p):
    '''obter_pos_l: posicao --> str.
    Funcao seletora do TAD posicao.
    Recebe uma posicao e retorna a linha que essa posicao ocupa.
    '''
    return p[1]


def eh_posicao(arg):
    '''eh_posicao: universal --> logico.
    Funcao reconhecedora do TAD posicao.
    Recebe um argumento e retorna o valor booleano da
    proposicao "Eh uma posicao?"
    '''
    return type(arg) == list and len(arg) == 2 and obter_pos_c(arg) in \
           ('a', 'b', 'c') and obter_pos_l(arg) in ('1', '2', '3')


def posicoes_iguais(p1, p2):
    '''posicao x posicao --> logico.
    Funcao teste do TAD posicao.
    Recebe duas posicoes e retorna o valor
    booleano da proposicao "Sao posicoes iguais?"
    '''
    return eh_posicao(p1) and eh_posicao(p2) and obter_pos_l(p1)\
           == obter_pos_l(p2) and obter_pos_c(p1) == obter_pos_c(p2)


def posicao_para_str(p):
    '''posicao_para_str: posicao --> str.
    Funcao transformadora do TAD posicao.
    Recebe uma posicao e retorna a representacao externa da posicao.
    '''
    return obter_pos_c(p) + obter_pos_l(p)


def tipo_posicao(p):
    '''tipo_posicao: posicao --> str.
    Funcao auxiliar do TAD posicao.
    Recebe uma posicao e retorna o tipo de posicao que esta representa.
    '''
    if eh_posicao(p):
        posicoes = ('canto', 'lateral', 'centro')
        if posicoes_iguais(p, cria_posicao('b', '2')): #centro
            return posicoes[2]
        elif p in (cria_posicao('a', '1'), cria_posicao('c', '1'), #posicoes
                   cria_posicao('a', '3'), cria_posicao('c', '3')):#centrais
            return posicoes[0]
        else: #laterais
            return posicoes[1]
    raise ValueError('tipo_posicao: argumento invalido')


def ordena_posicoes(posicoes):
    '''ordena_posicoes: lista de posicoes --> lista de posicoes.
    Funcao auxiliar do TAD posicao.
    Recebe uma lista que contem posicoes e retorna uma lista com os elementos
    da lista inicial mas por ordem em relacao ao tabuleiro.
    '''
    res = ()
    posicoestotais = (cria_posicao('a', '1'), cria_posicao('b', '1'),
                      cria_posicao('c', '1'), cria_posicao('a', '2'),
                      cria_posicao('b', '2'), cria_posicao('c', '2'),
                      cria_posicao('a', '3'), cria_posicao('b', '3'),
                      cria_posicao('c', '3'))
    for pos in posicoestotais:
        if pos in posicoes:
            res += (pos, )
    return res


def obter_posicoes_adjacentes(p):
    '''obter_posicoes_adjacentes: posicao --> lista de posicoes.
    Funcao de alto nivel do TAD posicao.
    Recebe uma posicao e retorna a lista que contem todas as
    posicoes adjacentes a posicao de entrada.
    '''
    if eh_posicao(p):
        pos = ()
        if tipo_posicao(p) == 'centro': #todas sao adjacentes ao centro
            return cria_posicao('a', '1'), cria_posicao('b', '1'), \
    cria_posicao('c', '1'), cria_posicao('a', '2'), cria_posicao('c', '2'), \
    cria_posicao('a', '3'), cria_posicao('b', '3'), cria_posicao('c', '3')
        elif tipo_posicao(p) == 'lateral':
            for i in (-1, 1): #posicoes "a esquerda e a direita"
                if eh_posicao([chr(ord(obter_pos_c(p)) + i), obter_pos_l(p)]):
                    pos += (cria_posicao(chr(ord(obter_pos_c(p)) + i),
                                         obter_pos_l(p)), )
            for i in (-1, 1): #posicoes "acima e abaixo"
                if eh_posicao([obter_pos_c(p), chr(ord(obter_pos_l(p)) + i)]):
                    pos += (cria_posicao(obter_pos_c(p),
                                         chr(ord(obter_pos_l(p)) + i)), )
        else:
            for i in (-1, 0, 1):     #posicoes em torno que sao posicoes validas
                for j in (-1, 0, 1): #e que nao sao a propria
                    if eh_posicao([chr(ord(obter_pos_c(p)) + i),
                                   chr(ord(obter_pos_l(p)) + j)]) and not \
                posicoes_iguais(p, cria_posicao(chr(ord(obter_pos_c(p)) + i),
                                                chr(ord(obter_pos_l(p)) + j))):
                        pos += (cria_posicao(chr(ord(obter_pos_c(p)) + i),
                                             chr(ord(obter_pos_l(p)) + j)), )
        return ordena_posicoes(pos)

#TAD peca
#Representacao interna: lista de um elemento na forma de cadeira de caracteres
# cria_peca: str --> peca
# cria_copia_peca: peca --> peca
# eh_peca: universal --> booleano
# pecas_iguais: peca x peca --> booleano
# peca_para_str: peca --> str
# peca_para_inteiro: peca --> int
# tabuleiros_iguais: tabuleiro x tabuleiro --> booleano

def cria_peca(s):
    '''cria_peca: chr --> peca.
    Funcao construtora do TAD peca.
    Recebe um caracter e retorna a peca correspondente.
    '''
    if s in ('X', ' ', 'O'):
        return [s]
    raise ValueError('cria_peca: argumento invalido')


def cria_copia_peca(j):
    '''cria_copia_peca: peca --> peca.
    Funcao construtora do TAD peca.
    Recebe uma peca e retorna uma copia dessa peca.
    '''
    if eh_peca(j):
        for peca in (cria_peca('X'), cria_peca(' '), cria_peca('O')):
            if pecas_iguais(peca, j):
                return peca
    raise ValueError('cria_copia_peca: argumento invalido')


def eh_peca(arg):
    '''eh_peca: universal --> logico
    Funcao reconhecedora do TAD peca.
    Recebe um argumento e retorna o valor booleano da proposicao "Eh uma peca?".
    '''
    return arg in (cria_peca('X'), cria_peca('O'), cria_peca(' '))


def pecas_iguais(p1, p2):
    '''pecas_iguais: peca x peca --> logico
    Funcao teste do TAD peca.
    Recebe duas pecas e retorna o valor booleano da
    proposicao "Sao pecas iguais?".
    '''
    return eh_peca(p1) and eh_peca(p2) and p1 == p2


def peca_para_str(j):
    '''peca_para_str: peca --> str
    Funcao transformadora do TAD peca.
    Recebe uma peca e retorna a cadeia de caracteres
    que a representa externamente.
    '''
    return '[' + j[0] + ']'


def peca_para_inteiro(j):
    '''peca_para_inteiro: peca --> int.
    Funcao de alto nivel do TAD peca.
    Recebe uma peca e retorna o inteiro que a representa.
    '''
    pecas = (cria_peca('O'), cria_peca(' '), cria_peca('X'))
    for i in range(3):
        if pecas_iguais(pecas[i], j):
            return i - 1

#TAD tabuleiro
#Representacao interna: dicionario com chaves em strings e com valores pecas
# cria_tabuleiro: {} --> tabuleiro
# cria_copia_tabuleiro: tabuleiro --> tabuleiro
# obter_peca: tabuleiro x posicao --> peca
# obter_vetor: tabuleiro x str --> tuplo de pecas
# coloca_peca: tabuleiro x posicao x peca --> tabuleiro
# remove_peca: tabuleiro x posicao --> tabuleiro
# move_peca: tabuleiro x posicao x posicao --> tabuleiro
# eh_tabuleiro: universal --> booleano
# eh_posicao_livre: tabuleiro x posicao --> booleano
# tabuleiro_para_str: tabuleiro --> str
# tuplo_para_tabuleiro: tuplo --> tabuleiro
# obter_ganhador: tabuleiro --> peca
# obter_posicoes_livres: tabuleiro --> tuplo de posicoes
# obter_posicoes_jogador: tabuleiro x peca --> tuplo de posicoes


def cria_tabuleiro():
    '''cria_tabuleiro: {} --> tabuleiro.
    Funcao construtora do TAD tabuleiro.
    Retorna um tabuleiro.
    '''
    return {'a1': cria_peca(' '), 'b1': cria_peca(' '), 'c1': cria_peca(' '),
            'a2': cria_peca(' '), 'b2': cria_peca(' '), 'c2': cria_peca(' '),
            'a3': cria_peca(' '), 'b3': cria_peca(' '), 'c3': cria_peca(' ')}


def cria_copia_tabuleiro(t):
    '''cria_copia_tabuleiro: tabuleiro --> tabuleiro.
    Funcao construtora do TAD tabuleiro.
    Recebe um tabuleiro e retorna um tabuleiro igual.
    '''
    if eh_tabuleiro(t):
        return {'a1': obter_peca(t, cria_posicao('a', '1')),
                'b1': obter_peca(t, cria_posicao('b', '1')),
                'c1': obter_peca(t, cria_posicao('c', '1')),
                'a2': obter_peca(t, cria_posicao('a', '2')),
                'b2': obter_peca(t, cria_posicao('b', '2')),
                'c2': obter_peca(t, cria_posicao('c', '2')),
                'a3': obter_peca(t, cria_posicao('a', '3')),
                'b3': obter_peca(t, cria_posicao('b', '3')),
                'c3': obter_peca(t, cria_posicao('c', '3'))}
    else:
        raise ValueError('cria_copia_tabuleiro: argumento invalido')


def obter_peca(t, p):
    '''obter_peca: tabuleiro x posicao --> peca
    Funcao seletora do TAD tabuleiro.
    Recebe um tabuleiro e uma posicao e retorna a peca
    que ocupa o tabuleiro na posicao desejada.
    '''
    return t[posicao_para_str(p)]


def obter_vetor(t, s):
    '''obter_vetor: tabuleiro x char --> tuplo de pecas
    Funcao seletora do TAD tabuleiro.
    Recebe um tabuleiro e um caracter que representa a linha/coluna
    desejada e retorna um tuplo com todas as pecasdesta linha/coluna.
    '''
    res = ()
    for pos in ('a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3'):
        if s in pos:
            res += (obter_peca(t, str_para_pos(pos)), )
    return res


def coloca_peca(t, j, p):
    '''coloca_peca: tabuleiro x peca x posicao --> tabuleiro
    Funcao modificadora do TAD tabuleiro.
    Recebe um tabuleiro, uma peca e uma posicao e coloca
    a peca na posicao desejada do tabuleiro.
    '''
    t[posicao_para_str(p)] = j
    return t


def remove_peca(t, p):
    '''remove_peca: tabuleiro x posicao --> tabuleiro.
    Funcao modificadora do TAD tabuleiro.
    Recebe um tabuleiro e uma posicao e limpa essa posicao do tabuleiro.
    '''
    return coloca_peca(t, cria_peca(' '), p)


def move_peca(t, p1, p2):
    '''move_peca: tabuleiro x posicao x posicao --> tabuleiro.
    Funcao modificadora do TAD tabuleiro.
    Recebe um tabuleiro e duas posicoes e move a peca que
    ocupa a primeira posicao para a segunda posicao.
    '''
    peca = obter_peca(t, p1) #no caso de pecas_iguais(p1, p2)
    remove_peca(t, p1)
    coloca_peca(t, peca, p2)
    return t


def eh_tabuleiro(arg):
    '''eh_tabuleiro: universal --> logico.
    Funcao reconhecedora do TAD tabuleiro.
    Recebe um argumento e retorna o valor
    booleano da proposicao "E um tabuleiro?"
    '''
    if type(arg) != dict or len(arg) != 9:
        return False
    for chave in arg:
        if chave not in \
                ('a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3'):
            return False
    numX, numO, ganhadores = 0, 0, 0
    for s in ('a', 'b', 'c', '1', '2', '3'):
        sum = 0
        for a in obter_vetor(arg, s):
            if a not in (cria_peca('X'), cria_peca(' '), cria_peca('O')):
                return False
            sum += peca_para_inteiro(a)
        if abs(sum) == 3: #verifica se ha um vencedor no vetor
            ganhadores += 1
    for s in ('a', 'b', 'c'):
        for a in obter_vetor(arg, s): #conta o numero de pecas de cada tipo
            if peca_para_inteiro(a) == 1:
                numX += 1
            elif peca_para_inteiro(a) == -1:
                numO += 1
    return ganhadores <= 1 and numX <= 3 and numO <= 3 and abs(numX - numO) <= 1


def eh_posicao_livre(t, p):
    '''eh_posicao_livre: tabuleiro x posicao -- > logico
    Funcao teste do TAD tabuleiro e do TAD posicao.
    Recebe um tabuleiro e uma posicao e retorna o
    valor booleano da proposicao "E uma posicao vazia?"
    '''
    return eh_posicao(p) and pecas_iguais(obter_peca(t, p), cria_peca(' '))


def tabuleiros_iguais(t1, t2):
    '''tabuleiros_iguais: tabuleiro x tabuleiro --> logico.
    Funcao teste do TAD tabuleiro.
    Recebe dois tabuleiros e retorna o valor booleano
    da proposicao "Sao tabuleiros e, nesse caso, sao iguais?".
    '''
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and t1 == t2


def tabuleiro_para_str(t):
    '''tabuleiro_para_str: tabuleiro --> str.
    Funcao transformadora do TAD tabuleiro.
    Recebe um tabuleiro e retorna a cadeira de caracteres que o representa.
    '''
    res = '   a   b   c\n1 '
    for pos in obter_vetor(t, '1'):
        res += peca_para_str(pos) + '-'
    res = res[:len(res) - 1] + '\n   | \ | / |\n2 '
    for pos in obter_vetor(t, '2'):
        res += peca_para_str(pos) + '-'
    res = res[:len(res) - 1] + '\n   | / | \ |\n3 '
    for pos in obter_vetor(t, '3'):
        res += peca_para_str(pos) + '-'
    return res[:len(res) - 1]


def tuplo_para_tabuleiro(tuplo):
    '''tuplo_para_tabuleiro: tuplo --> tabuleiro.
    Funcao transformadora do TAD tabuleiro.
    Recebe um tuplo e retorna o tabuleiro correspondente.
    '''
    t = cria_tabuleiro()
    j = 0 #indice da linha
    for linha in tuplo:
        i = 0 #indice da coluna
        for peca in linha:
            simbolo = ''
            if peca == 1:
                simbolo = cria_peca('X')
            elif peca == 0:
                simbolo = cria_peca(' ')
            else:
                simbolo = cria_peca('O')
            coloca_peca(t, simbolo, cria_posicao(chr(ord('a') + i),
                                                 chr(ord('1') + j)))
            i += 1
        j += 1
    return t


def obter_ganhador(t):
    '''obter_ganhador: tabuleiro --> peca.
    Funcao de alto nivel do TAD tabuleiro.
    Recebe um tabuleiro e retorna a peca do jogador
    vitorioso ou a peca vazia caso este nao exista.
    '''
    for s in ('a', 'b', 'c', '1', '2', '3'):
        sum = 0
        for peca in obter_vetor(t, s):
            sum += peca_para_inteiro(peca) #soma os valores inteiros correspon-
        if abs(sum) == 3:                  #-dentes das pecas do vetor
            if sum == 3:
                return cria_peca('X')
            else:
                return cria_peca('O')
    return cria_peca(' ')


def obter_posicoes_livres(t):
    '''obter_posicoes_livres: tabuleiro --> tuplo.
    Funcao de alto nivel do TAD tabuleiro.
    Recebe um tabuleiro e retorna um tuplo
    com todas as posicoes que estejam vazias.
    '''
    res = ()
    for s in ('a', 'b', 'c'):
        i = 1 #indice da linha
        for peca in obter_vetor(t, s):
            if pecas_iguais(peca, cria_peca(' ')):
                res += (cria_posicao(s, str(i)), ) #posicao livre
            i += 1
    return ordena_posicoes(res)


def str_para_pos(pos):
    '''str_para_pos: cc --> posicao.
    Funcao construtora do TAD posicao.
    Recebe uma cadeira de caracteres e retorna a posicao correspondente.
    '''
    return cria_posicao(pos[0], pos[1])


def obter_posicoes_jogador(t, j):
    '''obter_posicoes_jogador: tabuleiro x peca --> tuplo de posicoes.
    Funcao de alto nivel do TAD tabuleiro.
    Recebe um tabuleiro e uma peca e retorna um tuplo
    com todas as posicoes que estejam ocupadas pela peca.
    '''
    res = ()
    for s in ('a', 'b', 'c'):
        i = 1
        for peca in obter_vetor(t, s):
            if pecas_iguais(peca, j):
                res += (cria_posicao(s, str(i)), ) #posicao de peca = j
            i += 1
    if res == ():
        return res
    return ordena_posicoes(res)


def obter_movimento_manual(t, j):
    '''obter_movimento_manual: tabuleiro x peca: tuplo de posicoes
    Funcao auxiliar.
    Recebe um tabuleiro e uma peca e retorna um tuplo com a posicao escolhida,
    manualmente, pelo jogador humano, ou um tuplo com duas posicoes que
    representam um movimento.
    '''
    res = ()
    if len(obter_posicoes_jogador(t, j)) < 3: #fase de colocacao
        pos = input('Turno do jogador. Escolha uma posicao: ')
        if pos not in ('a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3') \
                or not eh_posicao_livre(t, str_para_pos(pos)):
            raise ValueError('obter_movimento_manual: escolha invalida')
        return str_para_pos(pos),
    pos = input('Turno do jogador. Escolha um movimento: ')
    if len(pos) == 4 and pos[2:] in ('a1', 'a2', 'a3', 'b1', 'b2', 'b3',
                                     'c1', 'c2', 'c3') and pos[:2] in \
    ('a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3'): #fase de movimento
        if pos[:2] == pos[2:] and str_para_pos(pos[:2]) in \
                obter_posicoes_jogador(t, j): #se o movimento for "nulo"
            for posadj in obter_posicoes_adjacentes(str_para_pos(pos[2:])):
                if eh_posicao_livre(t, posadj): #se ha posicao adjacente livre
                    raise ValueError('obter_movimento_manual: escolha invalida')
            return str_para_pos(pos[:2]), str_para_pos(pos[2:])
        elif eh_posicao_livre(t, str_para_pos(pos[2:])) and \
                str_para_pos(pos[:2]) in obter_posicoes_jogador(t, j) and \
    str_para_pos(pos[2:]) in obter_posicoes_adjacentes(str_para_pos(pos[:2])):
            return str_para_pos(pos[:2]), str_para_pos(pos[2:])
    raise ValueError('obter_movimento_manual: escolha invalida')


def vitoria(t, j):
    '''vitoria:  tabuleiro x peca --> inteiro ou tuplo.
    Funcao auxiliar.
    Recebe um tabuleiro e uma peca e retorna um tuplo com a posicao onde
    o jogador com a peca de entrada deve jogar de modo a ganhar o jogo.
    '''
    for s in ('a', 'b', 'c'):
        sum = 0
        indice = 0
        res = ()
        for peca in obter_vetor(t, s):
            sum += peca_para_inteiro(peca)
            if pecas_iguais(peca, cria_peca(' ')): #guarda a ultima posicao
                res = (cria_posicao(s, str(indice + 1)),) #vazia iterada
            indice += 1
        if sum == 2 * peca_para_inteiro(j): #se a peca estiver a ganhar
            return res                      #retorna a utima posicao vazia
    for s in ('1', '2', '3'): #mesma coisa que o codigo acima
        sum = 0               #necessita ser copiado devido a mudanca na
        indice = 0            #ultima posicao vazia iterada
        res = ()
        for peca in obter_vetor(t, s):
            sum += peca_para_inteiro(peca)
            if pecas_iguais(peca, cria_peca(' ')):
                res = (cria_posicao(chr(ord('a') + indice), s), )
            indice += 1
        if sum == 2 * peca_para_inteiro(j):
            return res
    return 0


def bloqueio(t, j):
    '''bloqueio: tabuleiro x peca --> inteiro ou tuplo
    Funcao auxiliar.
    Recebe um tabuleiro e uma peca e retorna um tuplo com a posicao onde o
    jogador com a peca de entrada deve jogar de modo a que o
    oponente nao venca na proxima jogada.
    '''
    return vitoria(t, inteiro_para_peca(-peca_para_inteiro(j)))


def canto(t):
    '''canto: tabuleiro --> inteiro ou tuplo.
    Funcao auxiliar.
    Recebe um tabuleiro e retorna o primeiro canto vazio
    ou o inteiro 0 caso este nao exista.
    '''
    for p in ('a1', 'c1', 'a3', 'c3'):
        if eh_posicao_livre(t, str_para_pos(p)):
            return str_para_pos(p),
    return 0


def lateral(t):
    '''lateral: tabuleiro --> inteiro ou tuplo.
    Funcao auxiliar.
    Recebe um tabuleiro e retorna a primeira lateral
    vazia ou o inteiro 0, caso esta nao exista.
    '''
    for p in ('b1', 'a2', 'c2', 'b3'):
        if eh_posicao_livre(t, str_para_pos(p)):
            return str_para_pos(p),
    return 0


def valor_tabuleiro(t):
    '''valor_tabyleiro: tabuleiro --> inteiro.
    Funcao auxiliar.
    Recebe um tabuleiro e retorna o valor correspondente da peca vencedora
    (0 se nao houver vencedor, 1 se o vencedor for a
    peca X e -1 se o vencedor for a peca O).
    '''
    return peca_para_inteiro(obter_ganhador(t))


def inteiro_para_peca(i):
    '''inteiro_para_peca: inteiro --> peca.
    Funcao construtora do TAD peca.
    Recebe um inteiro e retorna a peca correspondente.
    '''
    return (cria_peca('O'), cria_peca(' '), cria_peca('X'))[i+1]

def minimax(t, j, profundidade, seq_movimentos):
    '''minimax: tabuleiro x peca x inteiro x tuplo --> tuplo
    Funcao auxiliar.
    Recebe um tabuleiro, uma peca, uma cadeia
    de caracteres e um tuplo e retorna um tuplo.
    '''
    if not pecas_iguais(obter_ganhador(t), cria_peca(' ')) or profundidade == 0:
        return valor_tabuleiro(t), seq_movimentos
    else:
        melhor_resultado = -peca_para_inteiro(j)
        melhor_seq_movimentos = ()
        for posi in obter_posicoes_jogador(t, j):
            for posf in obter_posicoes_adjacentes(posi):
                if eh_posicao_livre(t, posf):
                    novo_tab=move_peca(cria_copia_tabuleiro(t), posi, posf)
                    novo_resultado, nova_seq_movimentos = \
            minimax(novo_tab, inteiro_para_peca(-peca_para_inteiro(j)),
                    profundidade - 1, seq_movimentos + (posi, posf))
                    if melhor_seq_movimentos == () or (pecas_iguais(j,
                    cria_peca('X')) and novo_resultado > melhor_resultado) or \
        (pecas_iguais(j, cria_peca('O')) and novo_resultado < melhor_resultado):
                        melhor_resultado = novo_resultado
                        melhor_seq_movimentos = nova_seq_movimentos
        return melhor_resultado, melhor_seq_movimentos    #retorna o melhor
# resultado e a melhor sequencia de movimentos para o tabuleiro e para a peca do
# jogador. Por recursao, acha o melhor movimento para cada peca colocada


def facil(t, j):
    '''facil: tabuleiro x peca --> tuplo.
    Funcao auxiliar.
    Recebe um tabuleiro e uma peca e retorna um movimento
    (tuplo que contem duas posicoes adjacentes).
    '''
    for pos in obter_posicoes_jogador(t, j):
        for posadj in obter_posicoes_adjacentes(pos):
            if eh_posicao_livre(t, posadj):
                return pos, posadj #primeira posicao adjacente livre
    pos = obter_posicoes_jogador(t, j)[0]
    return pos, pos


def obter_movimento_auto(t, j, modo):
    """obter_movimento_auto: tabuleiro x peca x string --> tuplo.
    Funcao auxliar.
    Recebe um tabuleiro, uma peca e uma cadeia de caracteres e retorna um tuplo
    com uma posicao ou um tuplo com duas posicoes"""
    if obter_posicoes_jogador(t, j) == 0 or len(obter_posicoes_jogador(t,j)) <3:
        if vitoria(t, j) != 0:                  # fase de colocacao, igual
            return vitoria(t, j)                # em todas as dificuldades
        elif bloqueio(t, j) != 0:
            return bloqueio(t, j)
        elif pecas_iguais(obter_peca(t,cria_posicao('b', '2')), cria_peca(' ')):
            return cria_posicao('b', '2'), #centro
        elif canto(t) != 0:
            return canto(t)
        else:
            return lateral(t)
    else: #fase de movimento
        if modo == 'facil':
            return facil(t, j)
        elif modo == 'normal':
            if minimax(t, j, 1, ())[1] != (): #existe melhor movimento
                return minimax(t, j, 1, ())[1][0], minimax(t, j, 1, ())[1][1]
            else:
                return obter_posicoes_jogador(t, j)[0], \
                       obter_posicoes_jogador(t, j)[0]
        elif modo == 'dificil':
            if minimax(t, j, 5, ())[1] != ():
                return minimax(t, j, 5, ())[1][0], minimax(t, j, 5, ())[1][1]
            else:
                return obter_posicoes_jogador(t, j)[0],\
                       obter_posicoes_jogador(t, j)[0]


def moinho(j, dificuldade):
    '''moinho: peca x str --> peca
    Funcao principal do programa, comeca o jogo.
    Recebe uma peca, a qual e atribuida ao jogador humano, e uma cadeia
    de caracteres que representa a dificuldade e inicia o jogo.'''
    if dificuldade not in ('facil', 'normal', 'dificil') \
            or j not in ('[X]', '[O]'):
        raise ValueError('moinho: argumentos invalidos')
    print('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade '+dificuldade +'.')
    if j == '[X]': #A peca [X] joga primeiro, a boolean humano decide quem joga
        humano, j, t = True, cria_peca('X'), cria_tabuleiro()
    else:
        humano, j, t = False, cria_peca('O'), cria_tabuleiro()
    print(tabuleiro_para_str(t))
    while valor_tabuleiro(t) == 0: #enquanto nao houver vencedor
        if humano: #turno do jogador humano
            pos, humano = obter_movimento_manual(t, j), False
            if len(pos) == 1: coloca_peca(t, j, pos[0]) #colocacao
            else: move_peca(t, pos[0], pos[1]) #movimento
            print(tabuleiro_para_str(t))
        else:
            pos, humano = obter_movimento_auto(t,
                    inteiro_para_peca(-peca_para_inteiro(j)), dificuldade), True
            if len(pos) == 1:  #colocacao
                coloca_peca(t, inteiro_para_peca(-peca_para_inteiro(j)), pos[0])
            else: move_peca(t, pos[0], pos[1]) #movimento
            print('Turno do computador (' + dificuldade + '):\n'
                  + tabuleiro_para_str(t))
    return '[' + obter_ganhador(t)[0] + ']'
