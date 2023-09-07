import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

estados = {
    'AP': 'Norte',
    'AC': 'Norte',
    'AM': 'Norte',
    'AL': 'Nordeste',
    'DF': 'Centro-Oeste',
    'ES': 'Sudeste',
    'CE': 'Nordeste',
    'BA': 'Nordeste',
    'MS': 'Centro-Oeste',
    'MA': 'Nordeste',
    'GO': 'Centro-Oeste',
    'MT': 'Centro-Oeste',
    'PA': 'Norte',
    'PE': 'Nordeste',
    'PB': 'Nordeste',
    'PI': 'Nordeste',
    'RJ': 'Sudeste',
    'MG': 'Sudeste',
    'RN': 'Nordeste',
    'RR': 'Norte',
    'RO': 'Norte',
    'PR': 'Sul',
    'SE': 'Nordeste',
    'SC': 'Sul',
    'TO': 'Norte',
    'RS': 'Sul',
    'SP': 'Sudeste'
}

def casos_confirmados_regiao(dataset):
    dataset_read = pd.read_csv(dataset)
    dadosOrg = dataset_read[['state', 'date', 'confirmed']]
    dadosOrg['date'] = pd.to_datetime(dadosOrg['date'])
    
    dadosOrg['regiao'] = dadosOrg['state'].map(estados)
    
    dados_agrupados = dadosOrg.groupby(['regiao', 'date'])['confirmed'].agg('sum').reset_index()
    plt.figure(figsize=(10, 10))
    sns.set(style="darkgrid")

    sns.lineplot(data=dados_agrupados, x='date', y='confirmed', hue='regiao')
    
    plt.ticklabel_format(axis='y', style='plain')
    plt.xlabel('Data')
    plt.ylabel('Casos')
    plt.title('Casos confirmados de Covid-19 por região', fontweight='bold', family='sans-serif')
    plt.legend(title='Região')
    plt.savefig('grafico_reg.png')
    plt.show()

casos_confirmados_regiao('casos.csv')
