'''
Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade
de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos
de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.
'''
from math import ceil

# Versão 1.0
cigarros_por_dia = 1
anos_fumantes = 1

tempo_perdido_por_cigarro = 10

tempo_perdido_em_minutos = cigarros_por_dia * (anos_fumantes * 365) * tempo_perdido_por_cigarro

tempo_perdido_em_horas = tempo_perdido_em_minutos / 60
tempo_perdido_em_dias = tempo_perdido_em_horas / 24

print('Esse fumante terá {} dias a menos de vida'.format(ceil(tempo_perdido_em_dias)))

