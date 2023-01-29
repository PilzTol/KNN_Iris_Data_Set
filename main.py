import csv
import random
import numpy as np

#Se eu quiser testar toda a base de testa posso iterar cada amostra da base de teste e adicionar os resultados em arquivos.
#Abre da base de teste e seleciona uma amostra aleatoriamente.
with open('iris_teste.csv', 'r') as iris_teste_csv:
    # ler arquivo csv inteiro em uma lista
    cobaias = list(csv.reader(iris_teste_csv))
    for cobaia in cobaias:    
        #Remove a classe da amostra em escolher_cobaia para não atrapalhar no cálculo das distâncias e salva a classe em uma variável para uso futuro.  
        classe_da_cobaia = cobaia[4]
        cobaia.remove(cobaia[4])
        cont = 0

        #Conversão de tipo de dado dos valores obtidos nos arquivos csv para que possam ser utilizados em "np.linalg.norm(np.array(linha) - np.array(escolher_cobaia))"
        for element in cobaia:
            cobaia[cont] = float(element)
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
                distance = np.linalg.norm(np.array(linha) - np.array(cobaia))
                #Adiciona a distância + classe da amostra em resultado.csv
                with open('distancias.csv', 'a', newline='') as distancias_csv:
                    escrever_distancia = csv.writer(distancias_csv)
                    escrever_distancia.writerow([distance, classe_da_linha])

        #Procura as distancias minimas com base no valor de K.
        with open('distancias.csv', 'r') as distancia_csv:
            leiura_distancias = list(csv.reader(distancia_csv))
        k = 15
        classe_distancia = 0
        while k !=0:
            min = leiura_distancias[0][0]
            for amostra in leiura_distancias:
                if amostra[0] < min:
                    min = amostra[0]
                    classe_distancia = amostra[1]
            leiura_distancias.remove([min,classe_distancia])
            k -=1
            with open('vizinhos_proximos.csv', 'a', newline='') as vizinhos_proximos_csv:
                escrever_vizinhos_proximos = csv.writer(vizinhos_proximos_csv)
                escrever_vizinhos_proximos.writerow([min,classe_distancia])

        #Limpa o arquivo "distancias.csv" para próxima iteração
        with open("distancias.csv", "w") as limpar_arquivo:
            limpar_arquivo.truncate()

        #Define qual a classe que a amostra pertence.
        with open('vizinhos_proximos.csv', 'r') as vizinhos_proximos_csv:
            leitura_vizinhos_proximos = list(csv.reader(vizinhos_proximos_csv))
        contagem = {}

        for sublist in leitura_vizinhos_proximos:
            contagem[sublist[1]] = contagem.get(sublist[1], 0) + 1
        elemento_mais_repetido = max(contagem, key=contagem.get)


        #O resultado está correto?
        acerto = 0
        if elemento_mais_repetido == classe_da_cobaia:
            acerto = 1
        else:
            acerto = 0

        #Limpa o arquivo "vizinhos_proximos.csv" para a próxima iteração
        with open("vizinhos_proximos.csv", "w") as limpar_arquivo:
            limpar_arquivo.truncate()
            
        #Adiciona os resultados do teste no arquivo.csv
        with open('resultado.csv', 'a', newline='') as resultado_csv:
                escrever_resultado = csv.writer(resultado_csv)
                escrever_resultado.writerow([elemento_mais_repetido, acerto])




        