# -*- coding: utf-8 -*-
"""aula03_CFADJP2021.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/clovesrocha/CFAD2021/blob/main/aula03_CFADJP2021.ipynb

#ETE PORTO DIGITAL
#CURSO DE FORMAÇÃO DE ANALISTA DE DADOS (JÚNIOR E PLENO 2021)
"""

#ETE PORTO DIGITAL
#CURSO DE FORMAÇÃO DE ANALISTA DE DADOS (JÚNIOR E PLENO 2021)

print('Olá mundo!')
print('Isso é Porto Digital!')
print('Vocês serão Analista de Dados!')

#mais códigos...

x = 'Cloves Rocha'
print(type(x))

x = 'Olá mundo!'
print(x)
print(type(x))

x = 2
y = 2
print(x == y)

x = 2**3
print(x)

x = 10//3 
print(x)

x = 10/3 
print(x)

x = 10%3 
print(x)

a = 3
b = 3
print(a >= b)

print('Olá mundo!, 2, 2.5, True, False')

numero = 2
print(f'O número {numero} é par.')

nome = input('Digite seu nome: ')
print(f'Seu nome é {nome}.')

matricula = input('Digite sua matrícula: ')
print(f'Sua matrícula é {matricula}.')

idade = input('Digite sua idade: ')
print(f'Você tem {idade} anos.')

idade = input('Digite sua idade: ')
print(f'Você tem {idade} anos.')
print(type(idade))

peso = float(input('Digite seu peso: '))
print(f'Você pesa {peso}KGs')
print(type(peso))

num = int(input('Digite um número: '))
if num % 2 == 0:
    print(f'O número {num} é par')
else:
    print(f'O número {num} é ímpar')

num = float(input('Digite um número: '))
#SE
if num > 0:
   print('Este número é positivo')

elif num == 0:
   print('Este número é neutro')

#SENAO
else:
   print('Este número é negativo')

resposta = int( input('Qual sua idade: ') )
if resposta >= 18 and resposta <= 65:
   print('Você é obrigado a votar!')
else:
   print('Você não é obrigado a votar!')

print('1. Idoso')
print('2. Gestante')
print('3. Cadeirante')
print('4. Nenhum destes')
resposta=int( input('Você é: ') )

if (resposta==1) or (resposta==2) or (resposta==3) :
   print('Você tem direito a fila prioritária')
else:
   print('Você não tem direito a nada. Vá pra fila e fique quieto')

a = 4
b = 2
print(not a > b)

banda = input('Qual melhor banda do mundo? ')

if not banda=='Beatles':
   print('Herege!')
else:
   print('Correto, são os Beatles!')

a = int(input('Digite um número: '))
if a in range(1, 300):
   print(f'{a} está entre 1 e 300.')
else:
   print(f'{a} não está entre 1 e 300.')