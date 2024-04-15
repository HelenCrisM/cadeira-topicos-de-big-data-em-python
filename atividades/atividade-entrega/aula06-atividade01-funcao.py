# SINTAXE B
# def calculaMedia(num1,num2):
#     media = (num1+num2)/2
#     print(f'A média dos números informados vale {media}')

# Exemplo:
# calculaMedia(4,6)

# Atividade 01:
# Escreva uma função que receba um número inteiro como parâmetro e informe se ele é positivo, negativo ou ZERO.

def define_number(number):
  if number == 0:
    print('Número é zero')
  elif number > 0:
    print('Número é positivo!')
  else: 
    print('Número é negativo!')


input_number = int(input('Digite um número inteiro: '))

define_number(input_number)

