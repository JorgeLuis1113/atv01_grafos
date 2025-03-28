#Código será rodado como script no prompt de comando
#Sendo o primeiro argumento o nome do script (main.py) e o segundo o nome da instância
import sys
import numpy as np

def le_instancia(instancia):
    matriz = np.loadtxt(instancia, dtype=int)
    return matriz

#Pega as dimensões da matriz
def pega_dimensoes(matriz):
    dimensoes = np.shape(matriz)
    return dimensoes

#Imprime a matriz e suas dimensões em um novo arquivo com o nome da instancia e as dimensoes da matriz
def salva_resultado(instancia, matriz, dimensoes):
    #Cria o nome do arquivo (nome da instancia e as dimensoes da matriz)
    resultado = nome_arquivo + " " + str(dimensoes[0]) + " " + str(dimensoes[1])

    with open(resultado, "w") as arquivo:
        arquivo.write(f"""A matriz presente no arquivo {nome_arquivo}
{str(matriz)}
tem dimensoes {dimensoes}""")

#Carrega a matriz presente na instância e aloca ela em matriz
if __name__=="__main__":
    nome_arquivo = sys.argv[1]

    #Carrega a matriz presente na instância e aloca ela em matriz
    matriz = le_instancia(nome_arquivo)

    dimensoes = pega_dimensoes(matriz)

    salva_resultado(nome_arquivo, matriz, dimensoes)











