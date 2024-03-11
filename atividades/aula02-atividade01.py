# Atividades - If/Elif/Else

# Atividade 1:
# Crie um algoritmo que peça o nome de dois times de futebol e quantos gols cada time fez na partida.
# Com os dados coletados, informe qual time venceu, qual time perdeu ou se houve empate.

nome_primeiro_time = input('Digite um nome de time de futebol: ')
quant_de_gols_primeiro_time = int(input('Digite a quantidade de gols que cada time fez na partida: '))
nome_segundo_time = input('Digite outro nome de time de futebol: ')
quant_de_gols_segundo_time = int(input('Digite a quantidade de gols que cada time fez na partida: '))

if (quant_de_gols_primeiro_time == quant_de_gols_segundo_time):
    print('Empate!!')
elif (quant_de_gols_primeiro_time > quant_de_gols_segundo_time):
    print(f'Time {nome_primeiro_time} venceu!!')
else: 
    print(f'Time {nome_segundo_time} venceu!!')


# Atividade 2:
# Solicite ao usuário a resposta (sim ou não) às perguntas abaixo e imprima a conclusão.
# 1) Febre alta?
# 2) Dores de cabeça?
# 3) Dores musculares?
# 4) Manchas vermelhas na pele?

# Conclusões: 
# a) Se o usuário responder sim a pelo menos três perguntas, informe que ele está com dengue e peça para ele procurar um médico.
# b) Se o usuário responder sim a duas ou menos, informe que ele deve ficar em repouso e continuar observando a evolução dos sistomas.


print('-----------------------------------------')
print('Questionário de sintomas da dengue')
print('Responda as seguintes perguntas: ')
print('Digite s para sim e n para não')

resposta_afirmativa = 0
resposta_febre_alta = input('Febre alta? [S/n] ')
resposta_dores_de_cabeca = input('Dores de cabeça? [S/n] ')
resposta_dores_musculares = input('Dores musculares? [S/n] ')
resposta_manchas_vermelhas_na_pele =  input('Manchas vermelhas na pele? [S/n] ')


if resposta_febre_alta in ['S', 's', '']:
    resposta_afirmativa += 1
    
if resposta_dores_de_cabeca in ['S', 's', '']:
    resposta_afirmativa += 1

if resposta_dores_musculares in ['S', 's', '']:
    resposta_afirmativa += 1

if resposta_manchas_vermelhas_na_pele in ['S', 's', '']:
    resposta_afirmativa += 1


if (resposta_afirmativa == 4):
    print('Você está com dengue, procure um médico!!')
elif (resposta_afirmativa == 0):
    print('Você não está com dengue!!')
elif (resposta_afirmativa >= 1):
    print('Você deve ficar em repouso e continuar observando a evolução dos sintomas.')
