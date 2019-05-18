'''
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o
carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.
'''

km_percorridos = 100
dias_carro = 2
valor_km = 0.15
valor_diaria = 60

valor_aluguel = km_percorridos * valor_km + dias_carro * valor_diaria

print('o valor do aluguel desta carro teve o total de: ', valor_aluguel)