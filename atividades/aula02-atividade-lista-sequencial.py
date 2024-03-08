# Aula 02 - Lista Sequencial

# 1) Faça um programa que mostre a mensagem "Alô mundo" na tela.

print('Alô mundo')

# 2) Faça um programa que peça um número e então mostre a mensagem 'O número informado foi [número]

number = int(input('Digite um número inteiro: '))

print(f'O número informado foi {number}')

# 3) Faça um programa que peça as 4 notas bimestrais e mostre a média.

primeira_nota = float(input('Digite a nota 1: '))
segunda_nota = float(input('Digite a nota 2: '))
terceira_nota = float(input('Digite a nota 3: '))
quarta_nota = float(input('Digite a nota 4: '))

sum_notas = primeira_nota + segunda_nota + terceira_nota + quarta_nota
media_notas = sum_notas/4

print('A média é: ', media_notas)


# 4) Faça um programa que converta metros para centimetros

metros = float(input('Digite o valor em metros: '))

metros_para_centrimetros = metros/100

print('O valor em centímetros é: ', metros_para_centrimetros)


# 5) Faça um programa que peça o raio de um círculo, calcule e mostre sua área.

raio_circulo = float(input('Digite o raio do circulo: '))
pi = 3.14

area_circulo = (2*pi)*raio_circulo

print('Área do circulo: ', area_circulo)

# 6) Faça um programa que calcule a área de um quadrado

lado_quadrado = float(input('Digite o lado do quadrado: '))

area_quadrado = lado_quadrado*lado_quadrado

print('Área do quadrado: ', area_quadrado)

# 7) Faça um programa que pergunte quanto você ganha por hora e o 
# numero de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês

valor_salario_hora = float(input('Digite quanto você ganha por hora: '))
num_horas_trabalhadas_mensal = float(input('Digite a quantidade de numero de horas trabalhadas no mês: '))

salario_mes = valor_salario_hora*num_horas_trabalhadas_mensal

print('Valor do seu salário no mês: ', salario_mes)

# 8) Faça um programa que peça a temperatura em grau F°, transforme e mostre- a temperatura em graus C°

temperatura_fahrenheit = int(input('Digite a temperatura em F°: '))

temperatura_celsius = 5* ((temperatura_fahrenheit-32)/9)

print('Temperatura em Celsius: ', temperatura_celsius)


# 9) Faça um programa que peça 2 números inteiros e um número real. 
# Calcule e mostre:

# a) o produto do dobro do primeiro com metade do segundo.
# b) a soma do triplo do primeiro com o terceiro.
# c) o terceiro elevado ao cubo.

primeiro_num = int(input('Digite um numero inteiro: '))
segundo_num = int(input('Digite outro numero inteiro: '))
terceiro_num = float(input('Digite um numero real: '))

primeira_equacao = (2*primeiro_num) * (segundo_num/2)
segunda_equacao = (3*primeiro_num) + terceiro_num
terceira_equacao = terceiro_num ** (1/3)

print('Valor da primeira equação: ', primeira_equacao)
print('Valor da segunda equação: ', segunda_equacao)
print('Valor da terceira equação: ', terceira_equacao)

# 10) Tendo como dados de entrada a altura de uma pessoa,
# construa um algoritmo que calcule seu peso ideal, 
# usando a seguinte fórmula: (72.7*altura) - 58

altura_usuario = float(input('Digite sua altura: '))

peso_ideal = (72.7*altura_usuario) - 58

print('Seu peso ideal é: ', peso_ideal)
