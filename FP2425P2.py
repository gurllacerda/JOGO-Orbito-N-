# TAD Posição -> Posição = tuplo(coluna, linha)
#CONSTRUTORES 
def cria_posicao(col,lin):
    """
    Cria uma posição no tabuleiro representada por um tuplo.

    Parâmetros:
        col(str): Caractere que representa a coluna (de 'a' a 'j').
        lin(int): Inteiro que representa a linha (de 1 a 10).

    Retornos:
        tuple: Tuplo (col, lin) representando a posição.

    Raises:
        ValueError: Se os argumentos não forem válidos (coluna fora do intervalo 'a' a 'j' ou linha fora do intervalo 1 a 10).
    """
    maxColuna =  ("a","b","c","d","e","f","g","h","i","j")
    maxLinha = (1,2,3,4,5,6,7,8,9,10)
    if type(col) != str or type(lin) != int or col not in maxColuna or int(lin) not in maxLinha:
        raise ValueError("cria_posicao: argumentos invalidos")
    
    tuplo_resposta = (col,lin)
    
    return tuplo_resposta     

#SELETORES
def obtem_pos_col(p):
    """
    Obtém a coluna de uma posição.

    Parâmetros:
        p(tuple): Posição, que é representada por um tuplo.

    Retornos:
        str: Coluna da posição.
    """
    return p[0]

def obtem_pos_lin(p):
    """
    Obtém a linha de uma posição.

    Parâmetros:
        p (tuple): Posição, que é representada por um tuplo.

    Retornos:
        int: Linha da posição.
    """
    return p[1]

#RECONHECEDOR 
def eh_posicao(arg):
    """
    Verifica se o argumento representa uma posição válida.

    Parâmetros:
        arg: Argumento a ser verificado, uma posição.

    Retornos:
        bool: True se o argumento é uma posição, False caso contrário.
    """
    if type(arg) == tuple and len(arg) == 2:
        if type(arg[0]) == str and len(arg[0]) == 1 and type(arg[1]) == int:
            return True
    return False    

def obtem_lista_coluna(n):
    """
    Obtém a lista do alfabeto das colunas, ao se basear pela órbita.

    Parâmetros:
        n(int): Número de órbitas.

    Retornos:
        tuple: Tuplo com as colunas válidas para o tabuleiro de tamanho n.
    """ 
    maxColunas = ("a","b","c","d","e","f","g","h","i","j")
    # numColunas,numLinhas = n*2
    colunas = ()
    for i in range(len(maxColunas)):
        if i < n*2:
            colunas += (maxColunas[i],)
    return colunas 

#TESTE
def posicoes_iguais(p1,p2):
    """
    Verifica se duas posições são iguais.

    Parâmetros:
        p1(tuple): Primeira posição.
        p2(tuple): Segunda posição.

    Retornos:
        bool: True se as posições são iguais, False caso contrário.
    """
    if eh_posicao(p1) and eh_posicao(p2):
        if p1[0] == p2[0] and p1[1] == p2[1]:
            return True
    return False

#TRANSFORMADORES
def posicao_para_str(p):
    """
    Converte uma posição para string equivalente a essa posição.

    Parâmetros:
        p(tuple): Posição representada por uma tupla (coluna, linha).

    Retornos:
        str: String da posição.
    """
    colunaPosicao = obtem_pos_col(p)
    linhaPosicao = obtem_pos_lin(p)
    res = ""
    res += colunaPosicao + str(linhaPosicao)
    return res

def str_para_posicao(s):
    """
    Converte uma string para uma posição.

    Parâmetros:
        s(str): String de uma posição.

    Retornos:
        tuple: Tupla representando a posição.

    """
    posicao = cria_posicao(s[0], int(s[1]))
    return posicao


# FUNÇÕES DE ALTO NÍVEL 

def eh_posicao_valida(p,n):
    """
    Verifica se uma posição é válida para um tabuleiro com n órbitas.

    Parâmetros:
        p(tuple): Posição representada por um tuplo.
        n(int): Número de órbitas no tabuleiro.

    Retornos:
        bool: True se a posição é válida, False caso contrário.
    """
    if not eh_posicao(p) or n < 2 or n > 5:
        return False
    colunas = obtem_lista_coluna(n)
    if (obtem_pos_col(p) not in colunas) or (obtem_pos_lin(p) not in range(1,n*2+1,1)):
        return False
    return True

def obtem_posicoes_adjacentes(p, n, d):
    """
    Obtém as posições adjacentes a uma posição, considerando as diagonais ou apenas posições ortogonais.

    Parâmetros:
        p(tuple): Posição base representada por uma tupla (coluna, linha).
        n(int): Número de órbitas no tabuleiro.
        d(bool): Se True, inclui posições diagonais se False, apenas as ortogonais.

    Retornos:
        tuple: Tuplo com as posições adjacentes à posição fornecida.
    """

    #n é igual ao numero de orbitas
    linhaPosicao = obtem_pos_lin(p)
    colunaPosicao = obtem_pos_col(p)
    colunas = obtem_lista_coluna(n)  
    tuplo_resposta = ()
    for i in range(len(colunas)):
        if colunas[i] == colunaPosicao:
            elemento = i
            break
    
    if d:  
        if linhaPosicao > 1:
            tuplo_resposta += (cria_posicao(colunaPosicao, linhaPosicao - 1),)  # Acima
        if linhaPosicao > 1 and elemento < len(colunas) - 1:
            tuplo_resposta += (cria_posicao(colunas[elemento + 1], linhaPosicao - 1),)  # Diagonal superior direita
        if elemento < len(colunas) - 1:
            tuplo_resposta += (cria_posicao(colunas[elemento + 1], linhaPosicao),)  # Direita
        if linhaPosicao < n * 2 and elemento < len(colunas) - 1:
            tuplo_resposta += (cria_posicao(colunas[elemento + 1], linhaPosicao + 1),)  # Diagonal inferior direita
        if linhaPosicao < n * 2:
            tuplo_resposta += (cria_posicao(colunaPosicao, linhaPosicao + 1),)  # Abaixo
        if linhaPosicao < n * 2 and elemento > 0:
            tuplo_resposta += (cria_posicao(colunas[elemento - 1], linhaPosicao + 1),)  # Diagonal inferior esquerda
        if elemento > 0:
            tuplo_resposta += (cria_posicao(colunas[elemento - 1], linhaPosicao),)  # Esquerda
        if linhaPosicao > 1 and elemento > 0:
            tuplo_resposta += (cria_posicao(colunas[elemento - 1], linhaPosicao - 1),)  # Diagonal superior esquerda
    else:  
        if linhaPosicao > 1:
            tuplo_resposta += (cria_posicao(colunaPosicao, linhaPosicao - 1),)  # Acima
        if elemento < len(colunas) - 1:
            tuplo_resposta += (cria_posicao(colunas[elemento + 1], linhaPosicao),)  # Direita
        if linhaPosicao < n * 2:
            tuplo_resposta += (cria_posicao(colunaPosicao, linhaPosicao + 1),)  # Abaixo
        if elemento > 0:
            tuplo_resposta += (cria_posicao(colunas[elemento - 1], linhaPosicao),)  # Esquerda
        

    return tuplo_resposta

def obtem_orbita(pos, n):
    """
    Calcula a órbita de uma posição em um tabuleiro de dimensão n x n.

    Parâmetros:
        pos(tuple): Posição representada por um tuplo.
        n(int): Dimensão do tabuleiro.

    Retornos:
        int: A órbita da posição, baseada na menor distância até as bordas.
    """

    #n aqui é a doimensão
    linha = obtem_pos_lin(pos)
    coluna_letra = obtem_pos_col(pos)
    
    coluna = ord(coluna_letra) - ord('a')
    
    # Calcula a órbita com base na menor distância até as bordas
    return min(linha - 1, n - linha, coluna, n - 1 - coluna)

def ordena_posicoes(tup, n):
    """
    Ordena as posições em um tabuleiro de acordo com a órbita, linha e coluna.

    Parâmetros:
        tup(tuple): Tuplo de posições a serem ordenadas.
        n(int): Número de órbitas no tabuleiro.

    Retornos:
        list: Lista de posições ordenadas da órbita mais a dentro, linha mais acima e coluna mais a esquerda.
    """

    #n aqui é orbita
    def sort_key(pos):
        # Calcula a órbita da posição
        orbita = obtem_orbita(pos, n*2)
        
        #usar a orbita negativa para por a orbita mais pequena pra frente, ordenando em ordem crescente sendo a ultima orbita a maior, a 0
        # Retorna a chave de ordenação: órbita negativa, linha, coluna
        return (-orbita, obtem_pos_lin(pos), obtem_pos_col(pos))
    
    posicoes_ordenadas = sorted(tup, key=sort_key)
    
    return posicoes_ordenadas

# TAD Pedra -> Pedra = int
#CONSTRUTORES

def cria_pedra_branca():
    """
    Cria uma representação para a pedra branca no jogo.

    Retornos:
        int: Representação da pedra branca, com valor -1.
    """

    #jogadoer com 'O' 
    return -1  

def cria_pedra_preta():
    """
    Cria uma representação para a pedra preta no jogo.

    Retornos:
        int: Representação da pedra preta, com valor 1.
    """

    #jogador com 'X
    return 1  

def cria_pedra_neutra():
    """
    Cria uma representação para uma posição neutra no tabuleiro.

    Retornos:
        int: Representação da posição neutra, com valor 0.
    """
    return 0 

# RECONHECEDORES
def eh_pedra(arg):
    """
    Verifica se o argumento é uma pedra.

    Parâmetros:
        arg: Argumento a ser verificado.

    Retornos:
        bool: True se o argumento é uma pedra válida (-1 ou 1), False caso contrário.
    """
    if type(arg) == int:
        if arg == -1 or arg==1:
            return True
    return False 

def eh_pedra_branca(p):
    """
    Verifica se a pedra é branca.

    Parâmetros:
        p(int): Pedra a ser verificada.

    Retornos:
        bool: True se a pedra é branca (-1), False caso contrário.
    """
    if p == -1:
        return True
    return False

def eh_pedra_preta(p):
    """
    Verifica se a pedra é preta.

    Parâmetros:
        p(int): Pedra a ser verificada.

    Retornos:
        bool: True se a pedra é preta (1), False caso contrário.
    """
    if p == 1:
        return True
    return False

#TESTE
def pedras_iguais(p1,p2):
    """
    Verifica se duas pedras são iguais.

    Parâmetros:
        p1(int): Primeira pedra.
        p2(int): Segunda pedra.

    Retornos:
        bool: True se as pedras são iguais, False caso contrário.
    """
    if eh_pedra(p1) and eh_pedra(p2):
        if p1 == p2:
            return True
    return False

#TRANSFORMADORES 
def pedra_para_str(p):
    """
    Converte a representação de uma pedra para uma string.

    Parâmetros:
        p(int): Pedra a ser transformada (-1 para branca, 1 para preta, 0 para neutra).

    Retornos:
        str: Representação da pedra como string ('O' para branca, 'X' para preta, ' ' para neutra).
    """
    if p == -1:
        return 'O'
    elif p == 1:
        return 'X'
    else:
        return ' '

# FUNÇÕES DE ALTO NÍVEL 
def eh_pedra_jogador(p):
    """
    Verifica se a pedra é de um jogador.

    Parâmetros:
        p(int): Representação da pedra.

    Retornos:
        bool: True se a pedra representa um jogador (branca ou preta), False caso contrário.
    """
    if p == -1 or p == 1:
        return True
    return False

def pedra_para_int(p):
    """
    Converte uma representação de pedra para um valor inteiro.

    Parâmetros:
        p (str): Representação da pedra em string.

    Retornos:
        int: Representação inteira da pedra (1 para preta, -1 para branca, 0 para neutra).
    """
    if eh_pedra_preta(p):
        return 1
    if eh_pedra_branca(p):
        return -1
    return 0


#TAD Tabuleiro -> Tabuleiro = Lista de Listas
#CONSTRUTORES 
def cria_tabuleiro_vazio(n):
    """
    Cria um tabuleiro vazio com dimensão n .

    Parâmetros:
        n(int): Número de órbitas do tabuleiro.

    Retornos:
        list: Tabuleiro vazio, representado por uma lista de listas com zeros.

    Raises:
        ValueError: Se o valor de n for inválido.
    """
    if n < 2 or n > 5 or type(n) != int:
        raise ValueError("cria_tabuleiro_vazio: argumento invalido")
    
    tabuleiro = [list(0 for i in range(n*2)) for j in range(n*2)]
    return tabuleiro

def cria_tabuleiro(n,tp,tb):
    """
    Cria um tabuleiro inicial com pedras brancas e pretas em posições especificadas.

    Parâmetros:
        n(int): Número de órbitas do tabuleiro.
        tp(tuple): Tuplo com posições de pedras pretas.
        tb(tuple): Tuplo com posições de pedras brancas.

    Retornos:
        list: Tabuleiro com pedras brancas e pretas nas posições especificadas.

    Raises:
        ValueError: Se os argumentos forem inválidos.
    """
    listaColunas = obtem_lista_coluna(n)
    if n < 2 or n > 5 or type(tb) != tuple: 
        raise ValueError("cria_tabuleiro: argumentos invalidos")
    for posicao in tb:
        if posicao in tp or not eh_posicao_valida(posicao,n):
            raise ValueError("cria_tabuleiro: argumentos invalidos")

    tabuleiro = cria_tabuleiro_vazio(n)
    for posicao in tb:
        posicaoLinhaPbB = obtem_pos_lin(posicao)
        posicaoColunaPbB = obtem_pos_col(posicao)
        colunaPosicaoNumericaTb = [col for col in range(len(listaColunas)) if listaColunas[col] == posicaoColunaPbB][0]
        tabuleiro[posicaoLinhaPbB-1][colunaPosicaoNumericaTb] = cria_pedra_branca()

    for posicao in tp:
        posicaoLinhaPbP = obtem_pos_lin(posicao)
        posicaoColunaPbP = obtem_pos_col(posicao)
        colunaPosicaoNumericaTp = [col for col in range(len(listaColunas)) if listaColunas[col] == posicaoColunaPbP][0]
        tabuleiro[posicaoLinhaPbP-1][colunaPosicaoNumericaTp] = cria_pedra_preta()

    return tabuleiro


def cria_copia_tabuleiro(t):
    """
    Cria uma cópia de um tabuleiro, preservando sua estrutura de lista de listas.

    Parâmetros:
        t (list): Tabuleiro original, representado como uma lista de listas.

    Retornos:
        list: Cópia do tabuleiro original.
    """
    lista_copia = []
    for linha in t:
        linha_copiada = []
        for coluna in linha:
            linha_copiada += (coluna,)

        lista_copia += (linha_copiada,)
    return lista_copia

#RECONHECEDOR
def eh_tabuleiro(arg):
    """
    Verifica se o argumento fornecido é um tabuleiro válido.

    Parâmetros:
        arg(any): Objeto a ser verificado.

    Retornos:
        bool: True se o argumento é um tabuleiro válido, False caso contrário.
    """
    if type(arg) !=list or len(arg) < 4 or len(arg) >10:
        return False
    
    else:
        for linha in range(len(arg)):
            if type(arg[linha]) != list or len(arg[linha]) != len(arg):
                return False
            else:
                for coluna in range(len(arg[linha])):
                    if type(arg[linha][coluna]) != int or -1 > arg[linha][coluna] or 1 < arg[linha][coluna]:
                        return False
    return True 

#SELETORES
def obtem_numero_orbitas(t):
    """
    Obtém o número de órbitas em um tabuleiro.

    Parâmetros:
        t (list): Tabuleiro representado como uma lista de listas.

    Retornos:
        int: Número de órbitas do tabuleiro.
    """
    orbitas = len(t) // 2

    return orbitas

def obtem_pedra(t,p):
    """
    Obtém a pedra da posição especificada do tabuleiro.

    Parâmetros:
        t(list): Tabuleiro representado como uma lista de listas.
        p(tuple): Posição no tabuleiro.

    Retornos:
        int: Representação da pedra (-1 para branca, 1 para preta, 0 para neutra).
    """
    colunaPosicaoLetra = obtem_pos_col(p)
    linhaPosicao = obtem_pos_lin(p)
    listaLetraColuna = obtem_lista_coluna(len(t)//2)
    for elemento in range(len(listaLetraColuna)):
        if listaLetraColuna[elemento] == colunaPosicaoLetra:
            colunaPosicaoNumerica = elemento 

    resposta = t[linhaPosicao -1][colunaPosicaoNumerica] #diminuir 1 por causa da indexação com 0
    if resposta == 1:
        return 1
    elif resposta == -1:
        return -1
    else:
        return 0



def obtem_dimensao_tab(t):
    """
    Obtém a dimensão de um tabuleiro.

    Parâmetros:
        t(list): Tabuleiro representado como uma lista de listas.

    Retornos:
        int: Dimensão do tabuleiro.
    """
    return len(t)

def obtem_linha_horizontal(t,p):
    """
    Obtém todas as pedras na linha horizontal da posição especificada.

    Parâmetros:
        t (list): Tabuleiro representado como uma lista de listas.
        p (tuple): Posição inicial.

    Retornos:
        tuple: Tuplo com todas as posições e pedras na linha horizontal da posição.
    """
    tuplo_resposta = ()
    numColunas = obtem_dimensao_tab(t)
    colunas = obtem_lista_coluna(obtem_numero_orbitas(t))
    linhaPosicao = obtem_pos_lin(p) 

    linhaPosicao = obtem_pos_lin(p)  
    
    for colunaPosicao in range(numColunas): 
        posicao = cria_posicao(colunas[colunaPosicao], linhaPosicao )  
        tuplo_resposta += ((posicao, obtem_pedra(t,posicao)),)  
    
    return tuplo_resposta
   
def obtem_linha_vertical(t,p):
    """
    Obtém todas as pedras na linha vertical da posição especificada.

    Parâmetros:
        t (list): Tabuleiro representado como uma lista de listas.
        p (tuple): Posição inicial.

    Retornos:
        tuple: Tuplo com todas as posições e pedras na linha vertical da posição.
    """
    tuplo_resposta = ()
    coluna = obtem_pos_col(p)
    
    for linha in range(len(t)):  
        posicao = cria_posicao(coluna, linha + 1) 
        tuplo_resposta += ((posicao, obtem_pedra(t,posicao)),)

    return tuplo_resposta

def obtem_linhas_diagonais(t, p):
    """
    Obtém todas as pedras nas diagonais principal e antidiagonal da posição especificada.

    Parâmetros:
        t (list): Tabuleiro representado como uma lista de listas.
        p (tuple): Posição inicial.

    Retornos:
        tuple: Dois tuplos, contendo as posições e pedras na diagonal principal e antidiagonal.
    """
    diagonal_principal = antidiagonal = ()
    colunaPosicaoStr = obtem_pos_col(p)
    linhaPosicao = obtem_pos_lin(p)
    colunasTabuleiro = obtem_lista_coluna(obtem_dimensao_tab(t) // 2)
    colunaPosicaoNumerica = [col for col in range(len(colunasTabuleiro)) if colunasTabuleiro[col] == colunaPosicaoStr][0] #compreensão para diminuir o numero de linhas
   
    linhaPosicaoCopia, colunaPosicaoCopia = linhaPosicao,colunaPosicaoNumerica
    while linhaPosicaoCopia >= 1 and colunaPosicaoCopia >= 0:
        posicaoAtual = cria_posicao(colunasTabuleiro[colunaPosicaoCopia],linhaPosicaoCopia)
        diagonal_principal = ((posicaoAtual,obtem_pedra(t,posicaoAtual)),) + diagonal_principal
        linhaPosicaoCopia -= 1
        colunaPosicaoCopia -= 1

    linhaPosicaoCopia,colunaPosicaoCopia = linhaPosicao+1 ,colunaPosicaoNumerica+1   
    while linhaPosicaoCopia <= obtem_dimensao_tab(t) and colunaPosicaoCopia < obtem_dimensao_tab(t):
        posicaoAtual = cria_posicao(colunasTabuleiro[colunaPosicaoCopia],linhaPosicaoCopia)
        diagonal_principal = diagonal_principal + ((posicaoAtual,obtem_pedra(t,posicaoAtual)),)
        linhaPosicaoCopia += 1
        colunaPosicaoCopia += 1

    linhaPosicaoCopia,colunaPosicaoCopia = linhaPosicao +1,colunaPosicaoNumerica -1 
    while linhaPosicaoCopia <= obtem_dimensao_tab(t) and colunaPosicaoCopia >= 0:
        posicaoAtual = cria_posicao(colunasTabuleiro[colunaPosicaoCopia],linhaPosicaoCopia)
        antidiagonal = ((posicaoAtual, obtem_pedra(t,posicaoAtual)),)  +  antidiagonal
        linhaPosicaoCopia += 1
        colunaPosicaoCopia -= 1

    linhaPosicaoCopia, colunaPosicaoCopia = linhaPosicao,colunaPosicaoNumerica
    while linhaPosicaoCopia >= 1 and colunaPosicaoCopia < obtem_dimensao_tab(t):
        posicaoAtual = cria_posicao(colunasTabuleiro[colunaPosicaoCopia],linhaPosicaoCopia)
        antidiagonal = antidiagonal  +  ((posicaoAtual,obtem_pedra(t,posicaoAtual)),)
        linhaPosicaoCopia -= 1
        colunaPosicaoCopia += 1


    return diagonal_principal, antidiagonal

def obtem_posicoes_pedra(t,j):
    """
    Obtém as posições no tabuleiro onde há pedras de um determinado jogador.

    Parâmetros:
        t (list): Tabuleiro representado como uma lista de listas.
        j (int): Valor da pedra do jogador (1 para jogador 1, -1 para jogador 2).

    Retornos:
        tuple: Tuplo ordenado das posições das pedras do jogador especificado.
    """
    tuplo_resposta = ()
    dimensao = obtem_dimensao_tab(t)
    colunasTabuleiro = obtem_lista_coluna(obtem_dimensao_tab(t) // 2) #obtem as colunas da lista de a ,b .... baseado na dimensão
    for linha in range(dimensao):
        for coluna in range(dimensao):
            posicao = cria_posicao(colunasTabuleiro[coluna],linha+1)
            if obtem_pedra(t,posicao) == j:
                tuplo_resposta += (posicao,)
            
    tuplo_ordenado = ordena_posicoes(tuplo_resposta,dimensao//2)
    return tuplo_ordenado


#MODIFICADORES
def coloca_pedra(t,p,j):
    """
    Coloca a pedra de um jogador em uma posição específica no tabuleiro.

    Parâmetros:
        t (list): Tabuleiro representado como uma lista de listas.
        p (tuple): Posição onde a pedra será colocada.
        j (int): Valor da pedra do jogador (1 para jogador 1, -1 para jogador 2).

    Retornos:
        list: O tabuleiro atualizado.
    """
    colunaPosicaoStr = obtem_pos_col(p)
    linhaPosicao = obtem_pos_lin(p)
    colunasTabuleiro = obtem_lista_coluna(obtem_numero_orbitas(t))
    colunaPosicaoNumerica = [col for col in range(len(colunasTabuleiro)) if colunasTabuleiro[col] == colunaPosicaoStr][0] #compreensão para diminuir o numero de linhas
    t[linhaPosicao-1][colunaPosicaoNumerica] = j

    return t 

def remove_pedra(t,p):
    """
    Remove a pedra de uma posição específica no tabuleiro, colocando uma pedra neutra.

    Parâmetros:
        t (list): Tabuleiro representado como uma lista de listas.
        p(tuple): Posição de onde a pedra será removida.

    """
    colunaPosicaoStr = obtem_pos_col(p)
    linhaPosicao = obtem_pos_lin(p)
    colunasTabuleiro = obtem_lista_coluna(obtem_numero_orbitas(t))
    colunaPosicaoNumerica = [col for col in range(len(colunasTabuleiro)) if colunasTabuleiro[col] == colunaPosicaoStr][0] #compreensão para diminuir o numero de linhas
    t[linhaPosicao-1][colunaPosicaoNumerica] = cria_pedra_neutra()

#TESTE
def tabuleiros_iguais(t1,t2):
    """
    Verifica se dois tabuleiros são iguais, considerando as posições das pedras.

    Parâmetros:
        t1 (list): Primeiro tabuleiro representado como uma lista de listas.
        t2 (list): Segundo tabuleiro representado como uma lista de listas.

    Retornos:
        bool: True se os tabuleiros forem iguais, False caso contrário.
    """
    if eh_tabuleiro(t1) and eh_tabuleiro(t2):
        if len(t1) == len(t2):
            if obtem_posicoes_pedra(t1, -1) == obtem_posicoes_pedra(t2, -1) and obtem_posicoes_pedra(t1, 1) == obtem_posicoes_pedra(t2, 1):
                return True
    return False 

#TRANSFORMADOR
def tabuleiro_para_str(t):
    """
    Converte o tabuleiro em uma representação de string.

    Parâmetros:
        t (list): Tabuleiro representado como uma lista de listas.

    Retornos:
        str: Representação em string do tabuleiro.
    """
    colunas = obtem_lista_coluna(obtem_numero_orbitas(t))
    numLinhas = numColunas = len(t)
    tabuleiroResposta = ""
    cabecalho = "    " + "   ".join(colunas)+"\n"   #junta com 3 espaços entre cada 
    tabuleiroResposta = cabecalho 

    for linha in range(numLinhas):
        if linha + 1 == 10:
            numeroLinha = "10"
        else:
            numeroLinha = "0" + str(linha + 1)
        linhaStr = numeroLinha + " "  
        for coluna in range(numColunas):
            pedra = obtem_pedra(t, (colunas[coluna], linha + 1))
            if pedra == 0:
                linhaStr += "[ ]"  
            elif pedra == -1:
                linhaStr += "[O]" 
            elif pedra == 1:
                linhaStr += "[X]"  

            if coluna < numColunas - 1:
                linhaStr += "-"
        if linha < numLinhas -1:  
            tabuleiroResposta += linhaStr + "\n"
        else:
            tabuleiroResposta += linhaStr
        
        if linha < numLinhas - 1:
            tabuleiroResposta += " "+"|".join(["   " for i in range(numColunas)])+"|" + "\n"

    return tabuleiroResposta

#FUNÇÕES DE ALTO NÍVEL
def move_pedra(t, p1, p2):
    """
    Move uma pedra de uma posição para outra no tabuleiro.

    Parâmetros:
        t (list): Tabuleiro representado como uma lista de listas.
        p1 (tuple): Posição inicial da pedra.
        p2 (tuple): Posição final da pedra.

    Retornos:
        list: O tabuleiro atualizado.
    """
    pedraP1 = obtem_pedra(t, p1)
    jogadorPedra = pedra_para_int(pedraP1)
    coloca_pedra(t, p2, jogadorPedra)
    coloca_pedra(t, p1, cria_pedra_neutra())

    return t

def obtem_posicoes_por_orbita(dimensaoTab, orbita):
    """
    Obtém as posições pertencentes a uma órbita específica no tabuleiro.

    Parâmetros:
        dimensaoTab (int): Dimensão do tabuleiro.
        orbita (int): Número da órbita para obter as posições.

    Retornos:
        tuple: Posições pertencentes à órbita especificada.
    """
    posicoesOrbita = ()
    colunas = obtem_lista_coluna(dimensaoTab//2)

    for linha in range(1, dimensaoTab+1):
        for colunaLetra in colunas:
            posicao = (colunaLetra, linha)
            

            if obtem_orbita(posicao, dimensaoTab) == orbita:
                posicoesOrbita += (posicao,)
    return posicoesOrbita

def obtem_quadrante(pos, dimensao):
    """
    Determina o quadrante da posição especificada no tabuleiro.

    Parâmetros:
        pos (tuple): Posição no tabuleiro.
        dimensao (int): Dimensão do tabuleiro.

    Retornos:
        int: Quadrante ao qual a posição pertence.
    """
    coluna = obtem_pos_col(pos)  
    linha = obtem_pos_lin(pos)    
    
    colunas = obtem_lista_coluna(dimensao // 2)  
    numeroColunas = len(colunas)  # Número total de colunas
    colunaIndex = colunas.index(coluna)

    
    meioColuna = numeroColunas // 2
    meioLinha = dimensao // 2

    # Determina o quadrante
    if linha <= meioLinha and colunaIndex >= meioColuna:
        return 1  # Quadrante 1
    elif linha <= meioLinha and colunaIndex < meioColuna:
        return 2  # Quadrante 2
    elif linha > meioLinha and colunaIndex < meioColuna:
        return 3  # Quadrante 3
    else:
        return 4  # Quadrante 4

def obtem_posicao_seguinte(t,p,s):
    """
    Obtém a próxima posição em uma órbita específica, com base no sentido.

    Parâmetros:
        t (list): Tabuleiro representado como uma lista de listas.
        p (tuple): Posição atual.
        s (bool): Sentido do movimento (True para horário, False para anti-horário).

    Retornos:
        tuple: Próxima posição na órbita especificada.
    """
    dimensao = obtem_dimensao_tab(t)
    orbitaPosicao = obtem_orbita(p,dimensao)    
    numeroOrbitas = obtem_numero_orbitas(t)
    linhaPosicao = obtem_pos_lin(p)
    colunaPosicao = obtem_pos_col(p)
    posicoesAdjacentes = obtem_posicoes_adjacentes(p,numeroOrbitas,False)
    posicoesAdjacentesOrbita = ()
    for posicao in posicoesAdjacentes:
        if obtem_orbita(posicao,dimensao) == orbitaPosicao:
            posicoesAdjacentesOrbita += (posicao,)

    linhaMinNaOrbita = min(obtem_pos_lin(posicao) for posicao in posicoesAdjacentesOrbita)
    colunaMinima = min(obtem_pos_col(posicao) for posicao in posicoesAdjacentesOrbita)
    quadrantePosicao = obtem_quadrante(p,dimensao)
    if quadrantePosicao == 1:
        if linhaPosicao != linhaMinNaOrbita:
            return posicoesAdjacentesOrbita[1] if s else posicoesAdjacentesOrbita[0]
        return posicoesAdjacentesOrbita[0] if s else posicoesAdjacentesOrbita[1] 
    if quadrantePosicao == 2:
        return posicoesAdjacentesOrbita[0] if s else posicoesAdjacentesOrbita[1]  
    if quadrantePosicao == 3:
        if colunaPosicao != colunaMinima:
            return posicoesAdjacentesOrbita[1] if s else posicoesAdjacentesOrbita[0]
        return posicoesAdjacentesOrbita[0] if s else posicoesAdjacentesOrbita[1] 
    if quadrantePosicao == 4:
        return posicoesAdjacentesOrbita[1] if s else posicoesAdjacentesOrbita[0]
    
def roda_tabuleiro(t):
    """
    Roda o tabuleiro em uma direção específica, sentido anti-horário.

    Parâmetros:
        t (list): Tabuleiro representado como uma lista de listas.

    Retornos:
        list: O tabuleiro atualizado após a rotação.
    """
    dimensao = obtem_dimensao_tab(t)
    colunas = obtem_lista_coluna(obtem_numero_orbitas(t))  # Colunas relevantes para o tabuleiro
    novo_tabuleiro = cria_copia_tabuleiro(t)  

    
    for linha in range(1, dimensao + 1):
        for colunaLetra in colunas:
            posicao = cria_posicao(colunaLetra, linha)  
            posicaoSeguinte = obtem_posicao_seguinte(t, posicao, False)  
            
            # Obtem a pedra na posição atual do tabuleiro original
            pedra_atual = obtem_pedra(t, posicao)
            coloca_pedra(novo_tabuleiro, posicaoSeguinte, pedra_atual)

    
    for linha in range(dimensao):
        for coluna in range(dimensao):
            t[linha][coluna] = novo_tabuleiro[linha][coluna]  

    return t
            

def eh_pedra_do_jogador(pedra, jog):
        """
    Verifica se uma pedra pertence ao jogador especificado.

    Parâmetros:
        pedra (int): Valor da pedra (1 ou -1).
        jog (int): Valor do jogador (1 ou -1).

    Retornos:
        bool: True se a pedra pertence ao jogador, False caso contrário.
    """
        
        if eh_pedra_jogador(jog):
            return (jog == -1 and eh_pedra_branca(pedra)) or (jog == 1 and eh_pedra_preta(pedra))

def verifica_linha_pedras(t,p,j,k):
    """
    Verifica se há pelo menos 'k' pedras consecutivas do jogador ao longo de uma linha, coluna ou diagonal.

    Parâmetros:
        t (list): Tabuleiro a ser percorrido.
        p (tuple): Posição inicial.
        j (int): Valor do jogador (1 ou -1).
        k (int): Quantidade mínima de pedras consecutivas necessárias.

    Retornos:
        bool: True se há pelo menos 'k' pedras consecutivas, False caso contrário.
    """
    # k = 2*n
    posicoesLinhaPosicao = obtem_linha_horizontal(t,p)
    posicoesColunasPosicao = obtem_linha_vertical(t,p)
    posicoesDiagonaisPosicao = obtem_linhas_diagonais(t,p)

    pedra = obtem_pedra(t,p)
    if not eh_pedra_do_jogador(pedra,j):
        return False
    

    def num_consecutivos(posicoes, j):
        #função auxiliar para determinar se existem k posições iguais consecutivas
        consecutivos = 0
        for posicao in posicoes:
            pedra = obtem_pedra(t, posicao[0])
            if eh_pedra_do_jogador(pedra, j):
                consecutivos += 1
                if consecutivos >= k:
                    return True
            else:
                consecutivos = 0
        return False
        

    return num_consecutivos(posicoesLinhaPosicao,j) or num_consecutivos(posicoesColunasPosicao,j) or  \
           num_consecutivos(posicoesDiagonaisPosicao[0],j) or num_consecutivos(posicoesDiagonaisPosicao[1],j)

#FUNÇÕES ADICIONAIS
def eh_vencedor(t,j):
    """
    Verifica se o jogador especificado é o vencedor.

    Parâmetros:
        t (list): Tabuleiro a ser percorrido.
        j (int): Valor do jogador (1 ou -1).

    Retornos:
        bool: True se o jogador é o vencedor, False caso contrário.
    """
    dimensao = obtem_dimensao_tab(t)
    colunas = obtem_lista_coluna(dimensao // 2)
    
    for linha in range(1,dimensao+1):
        for coluna in range(len(colunas)):
            posicao = cria_posicao(colunas[coluna],linha)
           
            if verifica_linha_pedras(t,posicao,j,dimensao):
                return True
    return False

def obtem_posicoes_neutras(t):
    """
    Obtém as posições neutras do tabuleiro.

    Parâmetros:
        t (list): Tabuleiro a ser percorrido.

    Retornos:
        tuple: Tuplo com as posições neutras do tabuleiro.
    """
    dimensao = obtem_dimensao_tab(t)
    colunas = obtem_lista_coluna(dimensao // 2)
    posicoes_neutras = ()
    for linha in range(1,dimensao+1):
        for coluna in range(len(colunas)):
            posicao = cria_posicao(colunas[coluna],linha)
            if obtem_pedra(t,posicao) == cria_pedra_neutra():
                posicoes_neutras += (posicao,)
    
    return posicoes_neutras

def eh_fim_jogo(t):
    """
    Verifica se o jogo chegou ao fim, seja por vitória ou ausência de posições neutras.

    Parâmetros:
        t (list): Tabuleiro a ser percorrido.

    Retornos:
        bool: True se o jogo chegou ao fim, False caso contrário.
    """
    if eh_vencedor(t,cria_pedra_branca()) or eh_vencedor(t, cria_pedra_preta()) or obtem_posicoes_neutras(t) == ():
        return True
    return False

def escolhe_movimento_manual(t):
    """
    Solicita ao jogador que escolha uma posição válida manualmente.

    Parâmetros:
        t (list): Tabuleiro representado como uma lista de listas.

    Retornos:
        tuple: Posição escolhida pelo jogador.
    """
    posicoesLivres = obtem_posicoes_neutras(t)
    colunas = obtem_lista_coluna(obtem_dimensao_tab(t) //2)
    posicao = input("Escolha uma posicao livre:")
   
    
    if  posicao[0] in colunas and posicao[1].isdigit():
        if eh_posicao_valida(str_para_posicao(posicao), obtem_dimensao_tab(t) //2) and len(posicao) == 2 and str_para_posicao(posicao) in posicoesLivres:
            return str_para_posicao(posicao)
    return escolhe_movimento_manual(t)

def escolhe_movimento_auto(t,j,str):
    """
    Escolhe automaticamente um movimento com base na dificuldade.

    Parâmetros:
        t (list): Tabuleiro representado como uma lista de listas.
        j (int): Valor do jogador (1 ou -1).
        dificuldade (str): Dificuldade do jogo ("facil" ou "normal").

    Retornos:
        tuple: Posição escolhida automaticamente.
    """
    if str == "facil":
        return estrategia_facil(t,j)
    if str == "normal":
        return estrategia_normal(t,j)
    

def estrategia_facil(t,j):
    """
    Realiza uma jogada automática na dificuldade 'fácil'.

    Parâmetros:
        t(list): Tabuleiro atual do jogo.
        j(int): Valor da pedra do jogador (1 ou -1).

    Retornos:
        Uma posição (tuplo) onde o jogador `j` deve colocar sua pedra para aumentar as chances de vitória.
    """
    numOrbitas = obtem_numero_orbitas(t)
    posicoesLivres = obtem_posicoes_pedra(t, cria_pedra_neutra())
    
    posicoesLivresSeguintes_lista = []
    for pos in posicoesLivres:
        posicoesLivresSeguintes_lista += [obtem_posicao_seguinte(t, pos, False)]
    posicoesLivresSeguintes = tuple(posicoesLivresSeguintes_lista) #obtem as posicoes livres do tabuleiro rodado

    tabuleiroSeguinte = roda_tabuleiro(cria_copia_tabuleiro(t))
    posicoesValidas = ()
    for posicao in range(len(posicoesLivres)):
        posicaoSeguinte = posicoesLivresSeguintes[posicao] #posição seguinte a cada posição livre do tabuleiro original
        for posicoesAdjacentes in obtem_posicoes_adjacentes(posicaoSeguinte, numOrbitas, True):
            if pedras_iguais(obtem_pedra(tabuleiroSeguinte, posicoesAdjacentes), j): #para cada posicao adjacente a posição seguinte, verifica se a pedra é de j 
                posicoesValidas += (posicoesLivres[posicao],) #se tiver mais de uma pedra que corresponda a isso tudo
                return ordena_posicoes(posicoesValidas, numOrbitas)[0] #ordena e retorna a primeira

    return ordena_posicoes(posicoesLivres,numOrbitas)[0] #senão apenas ordena as posições livres e retorna a primeira 

def estrategia_normal(tab, pedra):
    """
    Realiza uma jogada na dificuldade 'normal'

    Parâmetros:
        tab(lista): Tabuleiro atual do jogo, representado como uma lista de listas.
        pedra(int): Valor da pedra do jogador (1 ou -1).

    Retornos:
        Uma posição (tupla) onde o jogador deve colocar sua pedra para maximizar o comprimento de sua linha
        ou bloquear a linha mais longa do adversário.
    """
    dimensao = obtem_dimensao_tab(tab)
    listaPosicoesLivre = obtem_posicoes_neutras(tab)
    posicaoResposta = None
    maximoLPossivel = 0

    tabuleiro_rotacionado = roda_tabuleiro(cria_copia_tabuleiro(tab))  # Apenas uma rotação
    for posicaoLivre in listaPosicoesLivre:
        posicaoSeguinte = obtem_posicao_seguinte(tab,posicaoLivre,False)
        tabuleiro_provisorio = cria_copia_tabuleiro(tabuleiro_rotacionado)
        coloca_pedra(tabuleiro_provisorio, posicaoSeguinte, pedra)
        
        # Simula a rotação do tabuleiro após a jogada
        for L in range(1, dimensao + 1):
            if verifica_linha_pedras(tabuleiro_provisorio, posicaoSeguinte, pedra, L):
                if L > maximoLPossivel:
                    maximoLPossivel = L
                    posicaoResposta = posicaoLivre

    if posicaoResposta is None or maximoLPossivel < dimensao:
        adversario = -pedra
        tabuleiro_rotacionado_adversario = roda_tabuleiro(roda_tabuleiro(cria_copia_tabuleiro(tab)))
        for posicaoLivre in listaPosicoesLivre:
            posicaoSeguinte2Rodadas = obtem_posicao_seguinte(tab, obtem_posicao_seguinte(tab,posicaoLivre,False), False)
            tabuleiro_provisorio_adversario = cria_copia_tabuleiro(tabuleiro_rotacionado_adversario)
            coloca_pedra(tabuleiro_provisorio_adversario, posicaoSeguinte2Rodadas, adversario)
            for L in range(1, dimensao + 1):
                if verifica_linha_pedras(tabuleiro_provisorio_adversario, posicaoSeguinte2Rodadas, adversario, L):
                    if L > maximoLPossivel:
                        maximoLPossivel = L
                        posicaoResposta = posicaoLivre

    if posicaoResposta is None and listaPosicoesLivre:
        posicaoResposta = ordena_posicoes(listaPosicoesLivre, dimensao)[0]
    return posicaoResposta


def verifica_modo(modo):
    """
    Verifica se o modo de jogo fornecido é válido (entre 'fácil', 'normal' ou '2jogadores').

    Parâmetros:
        modo(str): String que representa o modo de jogo escolhido.

    Retornos:
        bool: True se o modo é válido, False caso contrário.
    """
    if type(modo) == str:
        if modo == "facil" or modo == "normal" or modo == "2jogadores":
            return True
    return False


def orbito(n, modo, jog):
    """
    Inicia e controla o fluxo de um jogo Orbito.
    
    Parâmetros:
    n (int): Número de órbitas no tabuleiro (dimensão do tabuleiro será 2*n).
    modo (str): Nível de dificuldade do jogo ('facil' ou outros níveis possíveis).
    jog (int): Pedra escolhida pelo jogador (1 para preto e -1 para branco).
    
    Retorno:
    int: Devolve o jogador que venceu, 1 para o jogador com pedras pretas (1) e -1 para o jogador com pedras brancas (-1),
         ou 0 em caso de empate.
    """
    if jog != 'X' and jog != 'O':
        raise ValueError("orbito: argumentos invalidos")
    if type(n) != int or n < 2 or n > 5 or not eh_tabuleiro(cria_tabuleiro_vazio(n))  or not verifica_modo(modo):
        raise ValueError("orbito: argumentos invalidos")


    tabuleiro = cria_tabuleiro_vazio(n)  

    turno = 1  
    if jog == 'X':
        jogador = cria_pedra_preta()
    else:
        jogador = cria_pedra_branca()
    
    print(f"Bem-vindo ao ORBITO-{n}.")
    print(f"Jogo contra o computador ({modo}).")
    print(f"O jogador joga com '{jog}'.")
    
    while not eh_fim_jogo(tabuleiro):
        print(tabuleiro_para_str(tabuleiro))  
        
        if turno == jogador:
            print("Turno do jogador.")
            posicaoEscolhida = escolhe_movimento_manual(tabuleiro)
        else:
            if modo == "facil":
                print("Turno do computador (facil):")
                posicaoEscolhida = estrategia_facil(tabuleiro, turno)
            elif modo == "normal":
                print("Turno do computador (normal):")
                posicaoEscolhida = estrategia_normal(tabuleiro, turno)
        
        coloca_pedra(tabuleiro, posicaoEscolhida, turno)  # Atualiza o tabuleiro com a jogada
        roda_tabuleiro(tabuleiro)   
        # Alterna o turno
        turno *= -1

    if eh_vencedor(tabuleiro,turno) and eh_vencedor(tabuleiro,turno * -1) or not obtem_posicoes_pedra(tabuleiro,cria_pedra_neutra()) :
            print(tabuleiro_para_str(tabuleiro))
            print("EMPATE")
            return 0
    elif eh_vencedor(tabuleiro,turno):
            print(tabuleiro_para_str(tabuleiro))
            if turno == jogador:
                print("VITORIA")
                return  pedra_para_int(cria_pedra_preta()) if jogador ==  pedra_para_int(cria_pedra_preta()) else  pedra_para_int(cria_pedra_branca())
            else:
                print("DERROTA")
                return  pedra_para_int(cria_pedra_branca()) if jogador ==  pedra_para_int(cria_pedra_preta()) else  pedra_para_int(cria_pedra_preta())
    print("EMPATE")
    return 0




