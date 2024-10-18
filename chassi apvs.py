import pandas as pd

tabela = pd.read_excel('C:\\Users\\Gabri\\Downloads\\projeto colunas.xlsx') #LOCAL ONDE SE ENCONTRA MINHA PLANILHA EXCEL, PASTA DE DOWNLOADS.
#LISTAS CRIADAS EM PYTHON, PARA ADICIONAR O CONTEUDO DAS COLUNAS
coluna1 = []
coluna2 = []
ambascolunas = []
for linha in tabela.index: #Usando Pandas e For, transformo o conteúdo das linhas da coluna em variável no python
    c1 = tabela.loc[linha, 'Coluna1'] #Transformando o conteúdo da coluna do excel (Coluna1) em uma variável(c1).
    coluna1.append(c1) #Adicionando a variável C1(conteúdo da Coluna1 do excel) na lista de coluna1.
    c2 = tabela.loc[linha, 'Coluna2']
    coluna2.append(c2)
for a in coluna1: #ADICIONANDO EM UMA VARIÁVEL DE LISTA, O ELEMENTO QUE TEM EM AMBAS AS COLUNAS.
    for b in coluna2:
        if a == b:
            ambascolunas.append(a)
for c in ambascolunas:#REMOVENDO DA COLUNA 1 e 2, OS ELEMTENTOS QUE TEM NAS 2 COLUNAS, ASSIM SOBRANDO APENAS OS QUE SÃO UNICOS DESSAS MESMAS COLUNAS.
    coluna1.remove(c)
    coluna2.remove(c)
print("Tem em ambas as colunas")
print(ambascolunas)
print("Tem apenas na coluna 1")
print(coluna1)
print("Tem apenas na coluna 2")
print(coluna2)

