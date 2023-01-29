import csv
from fun import *
import numpy as np

#Abre da base de teste e seleciona uma amostra aleatoriamente.
with open('iris_teste.csv', 'r') as iris_teste_csv:
    # ler arquivo csv inteiro em uma lista
    cobaia_escolhida = list(csv.reader(iris_teste_csv))
    # Escolher um linha do arquivo csv aleatoriamente
    cobaia_escolhida = cobaia_escolhida[random.randint(1, 30)]

#Remove a classe da amostra em escolher_cobaia para não atrapalhar no cálculo das distâncias e salva a classe em uma variável para uso futuro.  
classe_da_cobaia = cobaia_escolhida[4]
cobaia_escolhida.remove(cobaia_escolhida[4])
cont = 0

#Conversão de tipo de dado dos valores obtidos nos arquivos csv para que possam ser utilizados em "np.linalg.norm(np.array(linha) - np.array(escolher_cobaia))"
for element in cobaia_escolhida:
    cobaia_escolhida[cont] = float(element)
    cont +=1

#Calcula as distancias da amostra escolhida e adiciona as distâncias no arquivo resultado.csv
with open('iris_treinamento.csv', 'r') as iris_treinamento_csv: 
    leitura_iris_treinamento = csv.reader(iris_treinamento_csv)
    for linha in leitura_iris_treinamento:
        #Remove a classe da amostra para calcular a distância e salva a classe em uma variável
        classe_da_linha = linha[4]
        linha.remove(linha[4])
        cont = 0
        #Conversão do tipo de dado
        for element in linha:
            linha[cont] = float(element)
            cont +=1
        distance = np.linalg.norm(np.array(linha) - np.array(cobaia_escolhida))
        #Adiciona a distância + classe da amostra em resultado.csv
        with open('distancias.csv', 'a', newline='') as distancias_csv:
            escrever_distancia = csv.writer(distancias_csv)
            escrever_distancia.writerow([distance, classe_da_linha])
        