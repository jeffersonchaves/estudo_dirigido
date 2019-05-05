'''
Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada
para a viagem.
'''

distancia_km = 10
velocidade_media = 80


tempo_viagem = distancia_km // velocidade_media

if distancia_km % velocidade_media:

    distancia_km_faltantes = distancia_km % velocidade_media
    tempo_viagem_min = int((distancia_km_faltantes / velocidade_media) * 60)

    print('tempo de viagem: {}h e {}min '.format(
        tempo_viagem, tempo_viagem_min))

else:
    print('tempo de viagem: {}hora(s)'.format(tempo_viagem))
