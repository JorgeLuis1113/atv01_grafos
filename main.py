#Transforma o código em scritp a ser rodado no prompt de comando
#Sendo o primeiro argumento o nome do script (main.py) e o segundo o nome da instância
import sys
nome_arquivo = sys.argv[1]

#Carrega a matriz presente na instância e aloca ela em matriz
import numpy as np
matriz = np.loadtxt(nome_arquivo, dtype = int)

#Pega as dimensões da matriz
dimensoes = np.shape(matriz)

#Cria o nome do arquivo (nome da instancia e as dimensoes da matriz)
resultado = nome_arquivo + " " + str(dimensoes[0]) + " " + str(dimensoes[1])


#Imprime a matriz e suas dimensões em um novo arquivo com o nome da instancia e as dimensoes da matriz
with open(resultado, "w") as arquivo:
    arquivo.write(f"""A matriz presente no arquivo {nome_arquivo}
{str(matriz)}
tem dimensoes {dimensoes}""")






