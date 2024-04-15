# Atividade 04 - Desafio
# Escreva uma função que receba um nome como parâmetro e informe quantas vogais existem nele.

vowel = 'aeiou'

def quant_vowel_func(name):
  quant_vowel = 0
  for letter in name:
    if letter in vowel: 
      quant_vowel += 1

  print(f'O nome tem {quant_vowel} vogais.')





name = input('Digite um nome: ')

quant_vowel_func(name)

