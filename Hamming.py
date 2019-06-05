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
    print('Palavra gerada {}' .format(resul))
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
    return resul


def Verificadora(verifica):
    aux = 0
    verifica.reverse()
    if verifica[0] == 1:
        aux += 8
    if verifica[1] == 1:
        aux += 4
    if verifica[2] == 1:
        aux += 2
    if verifica[3] == 1:
        aux += 1
    print('ResulVerificacao {}' .format(aux))
    return aux


def Correcao(ValorResultante, palavra):

    if palavra[ValorResultante - 1] == 1:
        palavra[ValorResultante - 1] = 0
    else:
        palavra[ValorResultante - 1] = 1
    return palavra


def CalculaG(substring):
    VarG = substring[0]
    for i in range(1, len(substring)):
        VarG = bool(VarG) ^ bool(substring[i])
    #print(int(VarG))

    return int(VarG)



def Decodifica(substring, MatrizReconhecedora):
    ValorGOriginal = substring[3]
    print('ValorGOriginal {}' .format(ValorGOriginal))
    NovaString = list()

    for i in range(4, len(substring)):
        NovaString.append(substring[i])

    print('NovaString {}' .format(NovaString))
    verifica = MultiVerificadora(NovaString, MatrizReconhecedora)
    print('verifica {}' .format(verifica))

    ValorResultante = Verificadora(verifica)

    ValorGRecalculado =CalculaG(NovaString)

    if ValorGRecalculado != ValorGOriginal:
        print('Dois erros deu ruim')
        salvaPalavraModificada(substring)
    else:
        if ValorResultante == 0:
            print('correto')
            salvaPalavraModificada(substring)
        else:
            ValorCorrigido = Correcao(ValorResultante, NovaString)
            print('Palavra Corrigida {}' .format(ValorCorrigido))
            salvaPalavraModificada(ValorCorrigido)


def salvaPalavra(PalavraFinal):
    arq = open('/home/fernando/Area de Trabalho/DadosFinais.thc','a')
    for i in range(0, len(PalavraFinal)):
        arq.writelines(str(PalavraFinal[i]))
    arq.close()


def salvaPalavraModificada(PalavraFinal):
    arq = open('/home/fernando/Area de Trabalho/DadosFinaisModificados.thc','a')
    for i in range(0, len(PalavraFinal)):
        arq.writelines(str(PalavraFinal[i]))
    arq.close()


def Codifica(substring, MatrizGeradora):

    PalavraFinal = list()
    palavra = list()
    palavra = MultiGeradora(substring, MatrizGeradora)
    G = CalculaG(palavra)
    print('Palavra {}' .format(palavra))
    PalavraFinal.append(0)
    PalavraFinal.append(0)
    PalavraFinal.append(0)
    PalavraFinal.append(G)
    palavra.reverse()
    for i in range(0, len(palavra)):
        PalavraFinal.append(palavra[i])
    salvaPalavra(PalavraFinal)
    print('L = Lixo\t G = Bit G\t P = Paridade\t D = Dados')
    print('             [L, L, L, G, P, P, D, P, D, D, D, P, D, D, D, D]')
    print('PalavraFinal {}' .format(PalavraFinal))


"""--------------------------------------------------------------------------------------------------"""
palavra = list()
string = list()
substring = list()
aux = 0
#op = int(input('Digite uma opção'))

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
            Codifica(substring, MatrizGeradora)
            #print(substring)

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
