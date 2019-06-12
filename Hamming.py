import sys

def MultiGeradora(vetor, MatrizGeradora):

    resul = list()
    aux = 0
    for i in range(0, len(MatrizGeradora)):
        for j in range(0, len(vetor)):
            aux += int(MatrizGeradora[i][j]) * int(vetor[j])
        aux = aux % 2
        resul.append(aux)
        aux = 0
    #print('Palavra gerada {}' .format(resul))
    return resul


def MultiVerificadora(palavra, MatrizReconhecedora):
    resul = list()
    aux = 0
    for i in range(0, len(MatrizReconhecedora)):
        for j in range(0, len(palavra)):
            aux += int(MatrizReconhecedora[i][j]) * int(palavra[j])
        aux = aux % 2
        resul.append(aux)
        aux = 0
        resul.reverse()
    return resul


def Verificadora(verifica):
    aux = 0
    #verifica.reverse()
    if verifica[0] == 1:
        aux += 8
    if verifica[1] == 1:
        aux += 4
    if verifica[2] == 1:
        aux += 2
    if verifica[3] == 1:
        aux += 1
    #print('ResulVerificacao {}' .format(aux))
    return aux


def Correcao(ValorResultante, palavra):

    #print('\n\n------------palavra[ValorResultante - 1]: {} '.format(palavra[ValorResultante - 1]))
    #print('Pos ini da palavra {}' .format(palavra.index(0)))
    #print('Pos ValorResultante da palavra {}' .format(palavra.index(ValorResultante - 1)))
    #print(type(palavra))
    #print(type( palavra[ValorResultante - 1]))
    #print('--Palavra {}' .format(palavra))
    if palavra[ValorResultante  - 1] == '1':
        #print('entrou na pos {}' .format((ValorResultante  - 1)))
        palavra[ValorResultante - 1] = '0'
    else:
        #print('---entrou na pos {}' .format((ValorResultante  - 1)))
        palavra[ValorResultante - 1] = '1'
    #print('--Palavra CORRIGIDA {}' .format(palavra))
    return palavra


def CalculaG(substring):
    substring = list(map(int, substring))
    #print('substring {} '.format(substring))
    VarG = substring[0]
    #print('substring[0] antes for{} '.format(substring[0]))

    for i in range(1, len(substring)):
        #print('VarG {} '.format(VarG))
        #print('substring[i]: {}' .format(substring[i]))
        VarG = (bool(VarG) ^ bool(substring[i]))
        #print('varg resul {}\n----------------------------------------------'.format(VarG))

    return int(VarG)
    
    '''
    substring = list(map(int, substring))
    print(type(substring))
    VarG = substring[0]
    #print('valor2 {} '.format(int(substring[0])))
    #print('valor {} '.format(bool(substring[0])))

    for i in range(1, len(substring)):
        int(VarG)
        vetor = substring[i]
        int(vetor)
        print('vetor {} e VarG {}' .format(type(vetor), type(VarG)))
        print('VarG {} '.format(VarG))
        print('substring[i]: {}' .format(vetor))

        if VarG == True and vetor == True:
            VarG = 0
        if VarG == 0 and vetor == 1:
            VarG = 1
        if VarG == 1 and vetor == 0:
            VarG = 1
        if VarG == 0 and vetor == 0:
            VarG = 0
        print('varg resul {}\n----------------------------------------------'.format(VarG))

    return int(VarG)
    '''

def Decodifica(substring, MatrizReconhecedora):
    PalavraFinal = list()
    print('L = Lixo\t G = Bit G\t P = Paridade\t D = Dados\n')
    print('             [ L ,  L ,  L ,  D ,  D ,  D ,  D ,  P ,  D ,  D ,  D ,  P ,  D ,  P ,  P ,  G ]')
    print('Palavra Lida {}\n' .format(substring))

    ValorGOriginal = substring[15]
    #print('-------ValorGOriginal {}' .format(ValorGOriginal))
    NovaString = list()

    for i in range(3, len(substring)-1):
        NovaString.append(substring[i])


    NovaString.reverse()
    #print('------NovaString 12 bits{}' .format(NovaString))
    verifica = MultiVerificadora(NovaString, MatrizReconhecedora)
    #print('------Verificacao {}' .format(verifica))

    ValorResultante = Verificadora(verifica)
    #print('------ValorResultante: Pos: {}' .format(ValorResultante))

    #print('------NovaString REVERSE {}' .format(NovaString))



    if ValorResultante == 0:
        print('Palavra Correta --- String Correta foi Salva ---')
        salvaPalavraModificada(substring)
    else:
        flag = True
        if ValorResultante < (len(NovaString)-1):
            ValorCorrigido = Correcao(ValorResultante, NovaString)
            ValorGRecalculado = CalculaG(ValorCorrigido)
            #print('Palavra (12 bits): {}' .format(ValorCorrigido))
            #print('------ValorGRecalculado {}' .format(ValorGRecalculado))
            
            PalavraFinal.append(0)
            PalavraFinal.append(0)
            PalavraFinal.append(0)

            ValorCorrigido.reverse()
            for i in range(0, len(ValorCorrigido)):
                PalavraFinal.append(ValorCorrigido[i])

            PalavraFinal.append(ValorGRecalculado)

        else:
            flag = False

        if flag == False:
            print('Dois Erros, Deu Ruim!!! --- String Salva com Erro ---')
            salvaPalavraModificada(substring)
        else:
            if int(ValorGRecalculado) != int(ValorGOriginal):
                print('Dois Erros, Deu Ruim!!! --- String Salva com Erro ---')
                salvaPalavraModificada(substring)
            else:
                print('Um Erro !!! --- String foi Corrigida ---')
                #print('L = Lixo\t G = Bit G\t P = Paridade\t D = Dados')
                print('                  [ L ,  L ,  L ,  D ,  D ,  D ,  D ,  P ,  D ,  D ,  D ,  P ,  D ,  P ,  P ,  G ]')
                print('Palavra Corrigida {}' .format(PalavraFinal))
                salvaPalavraModificada(PalavraFinal)


def salvaPalavra(PalavraFinal):
    arq = open('DadosFinais.thc','a')
    for i in range(0, len(PalavraFinal)):
        arq.writelines(str(PalavraFinal[i]))
    arq.close()


def salvaPalavraModificada(PalavraFinal):
    arq = open('DadosFinaisModificados.thc','a')
    for i in range(0, len(PalavraFinal)):
        arq.writelines(str(PalavraFinal[i]))
    arq.close()


def Codifica(substring, MatrizGeradora):

    PalavraFinal = list()
    palavra = list()
    #print('Substring {}' .format(substring))
    #palavra.reverse()
    substring.reverse()
    palavra = MultiGeradora(substring, MatrizGeradora)
    G = CalculaG(palavra)
    print('Palavra {}' .format(palavra))

    PalavraFinal.append(0)
    PalavraFinal.append(0)
    PalavraFinal.append(0)

    palavra.reverse()
    for i in range(0, len(palavra)):
        PalavraFinal.append(palavra[i])

    PalavraFinal.append(G)

    salvaPalavra(PalavraFinal)

    #palavra.reverse()

    print('L = Lixo\t G = Bit G\t P = Paridade\t D = Dados')
    print('             [L, L, L, D, D, D, D, P, D, D, D, P, D, P, P, G]')
    print('PalavraFinal {}' .format(PalavraFinal))


"""--------------------------------------------------------------------------------------------------"""
palavra = list()
string = list()
substring = list()
aux = 0

MatrizGeradora = [['1', '1', '0', '1', '1', '0', '1', '0'],
                  ['1', '0', '1', '1', '0', '1', '1', '0'],
                  ['1', '0', '0', '0', '0', '0', '0', '0'],
                  ['0', '1', '1', '1', '0', '0', '0', '1'],
                  ['0', '1', '0', '0', '0', '0', '0', '0'],
                  ['0', '0', '1', '0', '0', '0', '0', '0'],
                  ['0', '0', '0', '1', '0', '0', '0', '0'],
                  ['0', '0', '0', '0', '1', '1', '1', '1'],
                  ['0', '0', '0', '0', '1', '0', '0', '0'],
                  ['0', '0', '0', '0', '0', '1', '0', '0'],
                  ['0', '0', '0', '0', '0', '0', '1', '0'],
                  ['0', '0', '0', '0', '0', '0', '0', '1']]

MatrizReconhecedora = [['1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0'],
                       ['0', '1', '1', '0', '0', '1', '1', '0', '0', '1', '1', '0'],
                       ['0', '0', '0', '1', '1', '1', '1', '0', '0', '0', '0', '1'],
                       ['0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1']]


if str(sys.argv[2]) == '-w':
    aux = 1
    ref_arquivo = open(str(sys.argv[1]) , "r")
    for linha in ref_arquivo:
        bit = linha.split()
        for bit in linha:
            string.append(bit[0])

    for j in range(0, len(string)):
        substring.append(string[j])
        if len(substring) == 8:
            #print('Substring {}' .format(substring))
            Codifica(substring, MatrizGeradora)
            substring.clear()
    ref_arquivo.close()

if sys.argv[2] == '-r':
    aux = 1
    ref_arquivo = open(str(sys.argv[1]), "r")
    for linha in ref_arquivo:
        bit = linha.split()
        for bit in linha:
            string.append(bit[0])

    for j in range(0, len(string)):
        substring.append(string[j])
        if len(substring) == 16:
            #print(substring)
            Decodifica(substring, MatrizReconhecedora)
            aux += 8
            substring.clear()
    ref_arquivo.close()

#print(string)
