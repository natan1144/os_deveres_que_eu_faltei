'''receber a distancia e o combustivel e falar a media '''
print('\nolá, gostaria de saber a media de km/l que o seu carro fez hoje?')
distancia = input('\nQuantos km você percorreu hoje?: ')
gas = input('\nQuantos litros de gasolina foram gastos?: ')
distancia = float(distancia)
gas = float(gas)
media = distancia/gas

'''fazendo a comparaçao dos numeros para exibir o devido resultado'''
if (media > 13):
    print(f'seu veiculo está acima da media, consumindo aproximadamente 1L a cada {media}km rodados')
else:
    print(f'seu carro está abaixo da media, usando 1L a cada {media}km rodados')