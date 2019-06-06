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
    #print('ResulVerificacao {}' .format(aux))
    return aux


def Correcao(ValorResultante, palavra):

    if palavra[ValorResultante - 1] == 1:
        palavra[ValorResultante - 1] = str(0)
    else:
        palavra[ValorResultante - 1] = str(1)
    return palavra


def CalculaG(substring):
    VarG = bool(substring[0])
    for i in range(1, len(substring)):
        if VarG == True and substring[i] == True:
            VarG = False
        if VarG == False and substring[i] == True:
            VarG = True
        if VarG == True and substring[i] == False:
            VarG = True
        if VarG == False and substring[i] == False:
            VarG = False

    return int(VarG)



def Decodifica(substring, MatrizReconhecedora):
    PalavraFinal = list()
    print('L = Lixo\t G = Bit G\t P = Paridade\t D = Dados')
    print('            [ L ,  L ,  L ,  D ,  D ,  D ,  D ,  P ,  D ,  D ,  D ,  P ,  D ,  P ,  P ,  G ]')
    print('Palavra Lida{}' .format(substring))

    ValorGOriginal = substring[15]
    #print('ValorGOriginal {}' .format(ValorGOriginal))
    NovaString = list()

    for i in range(3, len(substring)-1):
        NovaString.append(substring[i])

    NovaString.reverse()
    verifica = MultiVerificadora(NovaString, MatrizReconhecedora)
    print('Verificacao {}' .format(verifica))

    ValorResultante = Verificadora(verifica)

    ValorGRecalculado = CalculaG(NovaString)
    #print('ValorGRecalculado {}' .format(ValorGRecalculado))

    if int(ValorGRecalculado) != int(ValorGOriginal):
        print('Dois Erros! Deu Ruim')
        salvaPalavraModificada(substring)
    else:
        if ValorResultante == 0:
            print('Palavra Correta')
            salvaPalavraModificada(substring)
        else:
            ValorCorrigido = Correcao(ValorResultante, NovaString)
            PalavraFinal.append(str(0))
            PalavraFinal.append(str(0))
            PalavraFinal.append(str(0))
            
            ValorCorrigido.reverse()
            for i in range(0, len(ValorCorrigido)):
                PalavraFinal.append(ValorCorrigido[i])

            PalavraFinal.append(str(ValorGRecalculado))
            print('L = Lixo\t G = Bit G\t P = Paridade\t D = Dados')
            print('                 [ L ,  L ,  L ,  D ,  D ,  D ,  D ,  P ,  D ,  D ,  D ,  P ,  D ,  P ,  P ,  G ]')
            print('Palavra Corrigida{}' .format(PalavraFinal))
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
