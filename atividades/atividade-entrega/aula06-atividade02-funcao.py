# Atividade 02:
# Crie uma função que receba dois números como parâmetros, verifique e retorne a quantidade (0, 1 ou 2) de números pares.

def quant_number_even(first_number, second_number):
  quant_number = 0
  if input_first_number % 2 == 0:
    quant_number += 1
  
  if input_second_number % 2 == 0:
    quant_number += 1
  
  print(quant_number)


input_first_number = int(input('Digite um número inteiro: '))
input_second_number = int(input('Digite outro número inteiro: '))

quant_number_even(input_first_number, input_second_number)

