# Abrindo o arquivo para leitura
#arq1 = open("C:/Users/Papai/Google Drive/5.Projetos/estudopy/estudopy/arquivos/arquivo1.txt", "r")
# Abrindo o arquivo para escrita
#arq2 = open("C:/Users/Papai/Google Drive/5.Projetos/estudopy/estudopy/arquivos/arquivo1.txt", "w")
#print(type(arq1))
#print(arq1)
#print(arq1.read())
#arq2.write("NOVA gravação")
#print(arq1.read())


import pandas as pd

#arquivo_csv = pd.read_csv("C:/Users/Papai/Google Drive/5.Projetos/estudopy/estudopy/arquivos/world_population.csv")
#arquivo_csv = pd.read_csv(
#        "C:/Users/Papai/Google Drive/5.Projetos/estudopy/estudopy/arquivos/titanic.csv",
#        encoding='utf-8',
#        dtype=str)
titanic = pd.read_csv("C:/Users/Papai/Google Drive/5.Projetos/estudopy/estudopy/arquivos/titanic.csv")
#print(arquivo_csv)
####exibir 8 primeiras linhas
#df = arquivo_csv.head(8)
#print(df)
####exibir 8 ultimas linhas
#df = arquivo_csv.tail(8)
#print(df)
####verificação de como os pandas interpretaram cada um dos tipos de dados 
# da coluna pode ser feita solicitando o atributo pandas dtypes:
#df = arquivo_csv.dtypes
#print(df)



#####CRIANDO arquivo XLSX APARTI DO CSV
from openpyxl import Workbook
#titanic.to_excel("C:/Users/Papai/Google Drive/5.Projetos/estudopy/estudopy/arquivos/titanic1.xlsx", sheet_name="passengers", index=False)



#####LENDO rquivo XLSX 
titanic1 = pd.read_excel("C:/Users/Papai/Google Drive/5.Projetos/estudopy/estudopy/arquivos/titanic1.xlsx", sheet_name="passengers")
#print(titanic1)


#####resumo técnico 
#titanic1.info()


#print(titanic1.head())


#######Resgantando a coluna idade
ages = titanic["Age"]
#print(ages.head())
#print(type(titanic["Age"]))
#print(titanic["Age"].shape)


age_sex = titanic[["Age", "Sex"]]
print(age_sex.head())
#print(arquivo_csv) 
#ou
#for item in arquivo_csv.values:
#    print(item)

