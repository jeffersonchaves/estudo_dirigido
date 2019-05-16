'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da
área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a
tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$25,00. 
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3
situações:

a. comprar apenas latas de 18 litros;
b. comprar apenas galões de 3,6 litros;
c. misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre
arredonde os valores para cima, isto é, considere latas cheias.
'''
from math import ceil

metros_quadrados = 109

# CONSTANTES
valor_lata = 80
valor_galao = 25

# converter para a mesma unidade de medida: nesse caso, mts quadrados
metros_cobertura_lata = 18 * 6
metros_cobertura_galao = 3.6 * 6


# a) comprar apenas latas de 18 litros
print("\n", "==*==" * 10, "\n")
# arredondou-se pra cima, já que não se pode comprar uma fração de uma lata ou galão
qtd_latas = ceil(metros_quadrados / metros_cobertura_lata)
custo_latas = qtd_latas * valor_lata

print("a) Para pintar {} metros de área, usando apenas latas".format(metros_quadrados))
print("serão necessárias {} latas ao custo de R${}".format(qtd_latas, custo_latas))


# b) comprar apenas galões de 3,6 litros
print("\n", "==*==" * 10, "\n")
qtd_galoes = ceil(metros_quadrados / metros_cobertura_galao)
custo_galoes = qtd_galoes * valor_galao

print("b) Para pintar {} metros de área, usando apenas galões".format(metros_quadrados))

print("Serão necessários {} galoes ao custo de R${}".format(
    qtd_galoes, custo_galoes))



# c. misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre
print("\n", "==*==" * 10, "\n")
metros_quadrados_disperdicio = metros_quadrados + \
    (metros_quadrados * 0.1)  # 10% de folga

qtd_latas = int(metros_quadrados_disperdicio / metros_cobertura_lata)
metros_quadrados_restantes = metros_quadrados_disperdicio % metros_cobertura_lata
qtd_galoes = ceil(metros_quadrados_restantes / metros_cobertura_galao)

print("c) Para pintar {} meetros de área usando latas e galões com acréscimo de 10%".format(metros_quadrados))
if qtd_galoes > 3 and qtd_latas == 0:
    qtd_lata = 1
    custo_lata = valor_lata

    print("Será necessário {} galão ao custo de R${}".format(qtd_lata, custo_lata))

else:
    custo_mesclado = qtd_galoes * valor_galao + qtd_latas * valor_lata
    print("Serão necessárias {} latas e {} galoes ao custo de R${}".format(
        qtd_latas, qtd_galoes, custo_mesclado))
