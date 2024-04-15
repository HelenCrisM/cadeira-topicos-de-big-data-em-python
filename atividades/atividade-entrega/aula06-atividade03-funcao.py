# Atividade 03:
# Escreva uma função que receba um número inteiro como parâmetro e informe se ele é par ou ímpar.

def number_odd_or_even(number):
  if number % 2 == 0:
    print('Número par')
  else:
    print('Número impar')


number = int(input('Digite um número inteiro: '))

number_odd_or_even(number)


