import pandas as pd
import win32com.client as win32

# importar a base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

# visualizar a base de dados
pd.set_option('display.max_columns', None)
print(tabela_vendas)

# faturamento por loja
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)

# quantidade de produtos vendidos por loja
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade)

print('-'*50)
# ticket médio por produto em cada loja
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
print(ticket_medio)

# enviar um email com o relatório
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'destinatário@outlook.com'
mail.Subject = 'Relatório de Vendas por Loja'
mail.HTMLBody = f'''
<p>Prezados,</p>

<p>Segue o Relatório de Vendas por Cada loja:</p>

<p>Faturamento:</p>
{faturamento.To_html()}

<p>Quantidade Vendida:</p>
{quantidade.To_html()}

<p>Ticket Médio dos Produtos em cada Loja:</p>
{ticket_medio.To_html()}

<p>Qualquer dúvida, estou à disposição.</p>

<p>Att.,</p>
<p>Remetente</p>
'''

mail.Send()

print('E-mail enviado!')