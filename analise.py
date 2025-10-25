import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Lendo o banco de dados
df = pd.read_csv("student-mat.csv")

#def visualizar_tabela(): 
 #   return print(df.head())


#Calcular a media das notas entre as idades
def media_notas_idade():
    medianotas = df.groupby('age')['G3'].mean().reset_index()
    sns.barplot(x = 'age', y = 'G3', data = medianotas, palette = 'viridis')
    plt.title("Média das notas entre as idades")
    plt.xlabel("Idade")
    plt.ylabel("Media da nota final G3")
    plt.show()

media_notas_idade()

#Calcular a média do consumo de álcool entre as idades 

def media_alcool_idade():
    media_alcool = df.groupby('age')[['Dalc', 'Walc']].mean().reset_index()

    # Transforma em formato "longo" para facilitar o uso no seaborn
    media_alcoolM = media_alcool.melt(id_vars='age', value_vars=['Dalc', 'Walc'], var_name='Tipo', value_name='Consumo Médio') #Deixando a tabela "larga" para ficar longa

    
    plt.figure(figsize=(8,5))
    sns.barplot(data=media_alcoolM, x='age', y='Consumo Médio', hue='Tipo', palette='viridis') #Plotando o grafico agora "alongado"

    plt.title('Consumo médio de álcool diário e semanal por idade')
    plt.xlabel('Idade')
    plt.ylabel('Consumo médio (escala 1–5)')
    plt.legend(title='Tipo de consumo')
    plt.show()

media_alcool_idade()

#Calcular a media das notas pelo consumo de álcool

def media_notas_alcool():
    medialcool = df.groupby('G3')[['Dalc', 'Walc']].mean().reset_index()
    
    #Alongando o dataframe

    medianotasM = medialcool.melt(id_vars = 'G3', value_vars = ['Dalc', 'Walc'], var_name = 'Tipo', value_name = 'Consumo Médio')

    plt.figure(figsize=(8,5))
    sns.barplot(data=medianotasM, x='G3', y='Consumo Médio', hue='Tipo', palette='viridis') #Plotando o grafico agora "alongado"

    plt.title('Consumo médio de álcool diário e semanal por notas')
    plt.xlabel('Notas')
    plt.ylabel('Consumo médio (escala 1–5)')
    plt.legend(title='Tipo de consumo')
    plt.show()

media_notas_alcool()

#Calcular faltas por idade:
def faltas_idades():
    faltasIdades = df.groupby('age')['absences'].mean().reset_index()
    sns.barplot(data=faltasIdades, x='age', y='absences', palette='viridis') 
    plt.title('Media da idade pelas faltas')
    plt.xlabel('Idade')
    plt.ylabel('Faltas')
    plt.show()
faltas_idades()

#Calcular a media das notas pelo consumo de álcool por idade

def faltas_alcool_idadeDiario():
    faltasidadeDiario = df.groupby('age').agg({'Dalc': 'mean', 'G3': 'mean', }).reset_index()
    

    plt.figure(figsize= (10,6))
    sns.scatterplot(data = faltasidadeDiario, x = 'age', y=  'G3', hue = 'Dalc', palette= 'viridis',size = 'Dalc' ,sizes=(50, 300))
    
    plt.title('Média das notas por idade e consumo de álcool')
    plt.xlabel('Idade')
    plt.ylabel('Média das Notas')
    plt.legend(title='Consumo')
    plt.show()

faltas_alcool_idadeDiario()




