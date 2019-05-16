'''
Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade
de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos
de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.
'''
from math import floor

# Verson 2.0
cigarros_por_dia = 1
anos_fumantes = 1

tempo_perdido_por_cigarro = 10

tempo_perdido_em_minutos = cigarros_por_dia * (anos_fumantes * 365) * tempo_perdido_por_cigarro

tempo_perdido_em_horas = tempo_perdido_em_minutos / 60
tempo_perdido_em_dias_inteiros = int(tempo_perdido_em_horas // 24)
tempo_perdido_em_dias_fracionados = tempo_perdido_em_horas % 24

print('Esse fumante terá {} dias e {} horas a menos de vida'.format(tempo_perdido_em_dias_inteiros, floor(tempo_perdido_em_dias_fracionados)))
