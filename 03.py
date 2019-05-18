'''
Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o
total em segundos.
'''

qtd_dias = 0
qtd_horas = 0
qtd_minutos = 1
qtd_segundos = 0

qtd_dias_segundos = qtd_dias * 24 * 60 * 60
qtd_horas_segundos = qtd_horas * 60 * 60
qtd_minutos_segundos = qtd_minutos * 60

total_em_segundos = qtd_dias_segundos + qtd_horas_segundos + qtd_minutos_segundos + qtd_segundos

print('quantidade de segundos: ', total_em_segundos)

