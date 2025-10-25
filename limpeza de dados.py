import pandas as pd

#Fazendo a limpeza de dados:
df = pd.read_csv("student-mat.csv")

fd = pd.read_csv("student-por.csv")


print(df.isna())
print(fd.isna())
print(df.info())
print(fd.info())

#Pode-se perceber que não há válidos nulos.