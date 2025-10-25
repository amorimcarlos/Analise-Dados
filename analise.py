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
    fig, ax = plt.subplots()
    sns.barplot(x = 'age', y = 'G3', data = medianotas, ax = ax)
    ax.set_title("Média das notas entre as idades")
    ax.set_xlabel("Idade")
    ax.set_ylabel("Media da nota final G3")
    #plt.show()
    return fig, medianotas

media_notas_idade()

#Calcular a média do consumo de álcool entre as idades 

def media_alcool_idade():
    media_alcool = df.groupby('age')[['Dalc', 'Walc']].mean().reset_index()
   
    # Transforma em formato "longo" para facilitar o uso no seaborn
    media_alcoolM = media_alcool.melt(id_vars='age', value_vars=['Dalc', 'Walc'], var_name='Tipo', value_name='Consumo Médio') #Deixando a tabela "larga" para ficar longa
    fig2, ax  = plt.subplots(figsize=(8,5))
    sns.barplot(data=media_alcoolM, x='age', y='Consumo Médio', hue='Tipo', palette='viridis', ax = ax) #Plotando o grafico agora "alongado"
    ax.set_title("Consumo médio de álcool diário e semanal por idade")
    ax.set_xlabel("Idade")
    ax.set_ylabel("Consumo médio")
    ax.legend(title='Tipo de consumo')
    #plt.show()
    return fig2, media_alcoolM

media_alcool_idade()

#Calcular a media das notas pelo consumo de álcool

def media_notas_alcool():
    medialcool = df.groupby('G3')[['Dalc', 'Walc']].mean().reset_index()
    
    #Alongando o dataframe

    medianotasM = medialcool.melt(id_vars = 'G3', value_vars = ['Dalc', 'Walc'], var_name = 'Tipo', value_name = 'Consumo Médio')

    fig3, ax = plt.subplots(figsize=(8,5))
    sns.barplot(data=medianotasM, x='G3', y='Consumo Médio', hue='Tipo', palette='viridis', ax = ax) #Plotando o grafico agora "alongado"

    ax.set_title("Consumo médio de álcool diário e semanal por notas")
    ax.set_xlabel("Notas")
    ax.set_ylabel("Consumo médio ")
    ax.legend(title="Tipo de consumo")
    #plt.show()
    return fig3, medianotasM

media_notas_alcool()

#Calcular a média faltas por idade:
def faltas_idades():
    faltasIdades = df.groupby('age')['absences'].mean().reset_index()
    fig4, ax = plt.subplots()
    sns.barplot(data=faltasIdades, x='age', y='absences', ax =ax ) 
    ax.set_title("Media da idade pelas faltas")
    ax.set_xlabel("Idade")
    ax.set_ylabel("Faltas")
    #plt.show()
    return fig4, faltasIdades
faltas_idades()

#Calcular a media das notas pelo consumo de álcool diário por idade

def faltas_alcool_idadeDiario():
    faltasidadeDiario = df.groupby('age').agg({'Dalc': 'mean', 'G3': 'mean', }).reset_index()
    

    fig5, ax = plt.subplots(figsize= (10,6))
    sns.scatterplot(data = faltasidadeDiario, x = 'age', y=  'G3', hue = 'Dalc', palette= 'viridis',size = 'Dalc' ,sizes=(50, 300), ax = ax)
    
    ax.set_title("Média das notas por idade e consumo de álcool")
    ax.set_xlabel("Idade")
    ax.set_ylabel("Média das Notas")
    ax.legend(title="Consumo de álcool diário")
    #plt.show()
    return fig5, faltasidadeDiario

faltas_alcool_idadeDiario()

#Calcular a media das notas pelo consumo de álcool semanal por idade

def faltas_alcool_idadeSemanal():
    faltasidadeSemanal = df.groupby('age').agg({'Walc': 'mean', 'G3': 'mean', }).reset_index()
    

    fig6, ax = plt.subplots(figsize= (10,6))
    sns.scatterplot(data = faltasidadeSemanal, x = 'age', y=  'G3', hue = 'Walc', palette= 'viridis',size = 'Walc' ,sizes=(50, 300), ax = ax)
    
    ax.set_title("Média das notas por idade e consumo de álcool")
    ax.set_xlabel("Idade")
    ax.set_ylabel("Média das Notas")
    ax.legend(title="Consumo de álcool semanal")
    #plt.show()
    return fig6, faltasidadeSemanal

faltas_alcool_idadeSemanal()






