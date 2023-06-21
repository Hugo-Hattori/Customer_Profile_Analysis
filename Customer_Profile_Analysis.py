import pandas as pd

#Passo 1: Importar a base de dados
tabela = pd.read_csv("clientes.csv", encoding="latin1", sep=";")

#Passo 2: Visualizar a base de dados
tabela = tabela.drop("Unnamed: 8", axis=1)
display(tabela)


#Passo 3: Tratamento de dados
tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")
display(tabela[tabela["Profissão"].isna()])
tabela = tabela.dropna()
print(tabela.info())


#Passo 4: Análise inicial -> entender as notas do clientes (avaliar a média como parâmetro)
display(tabela.describe())
#A média das notas é de em torno de 52 (principal parâmetro de comparação)


#Passo 5: Análise completa -> entender como a característica do cliente impacta na nota
import plotly.express as px

for coluna in tabela.columns:
    #cria o gráfico
    grafico = px.histogram(tabela, x=coluna, y="Nota (1-100)", text_auto=True, histfunc='avg', nbins=10)

    #mostrar o gráfico
    grafico.show()


#Correção de problema de exibição dos gráficos
import plotly.io as pio

pio.renderers.default='notebook'


# ## Resultado da análise: perfil ideal do cliente
# 
# - Acima de 15 anos (não tem muita diferença entre as faixas etárias depois disso)
# - Faixa salarial não parece fazer tanta diferença
# - Áreas de trabalho: Entretenimento e Artista (evitar Construção)
# - Tem entre 10 a 15 anos de experiência
# - Com famílias não tão grandes (até no máximo 7 pessoas)
