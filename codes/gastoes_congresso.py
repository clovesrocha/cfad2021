# -*- coding: utf-8 -*-
"""Gastoes_Congresso.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19om-Qos-OzsHlXCnQwlOkY9JRIXmulqL
"""

#ETE PD - Prof. Cloves Rocha
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

requests.get('http://meucongressonacional.com/senador')

soup = BeautifulSoup(content, 'html.parser')
table = soup.find(name='table')

table_str = str(table)
df = pd.read_html(table_str)[0]

df_ordenado = df.sort_values(by='R$/dia', ascending=[False])

df_ordenado.columns = ['Senador', 'Gabinete', 'Partido', 'Gasto_dia', 'Gastos']

df_ordenado2 = df_ordenado.drop(columns=['Gastos'])

df_ordenado3 = df_ordenado2[0:10]

print(df_ordenado3)

plt.rcdefaults()
fig, ax = plt.subplots()

ax.barh(Senador, Gasto_dia)
ax.set_yticks(Senador)
ax.set_ylabel('Senadores')
ax.invert_yaxis()
ax.set_xlabel('Gasto por Dia em R$')
ax.set_title('Quem são os 10 maiores Gastões?')
plt.show()
