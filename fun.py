import csv

def ler_data_set():
    with open("iris.csv", "r") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha)    