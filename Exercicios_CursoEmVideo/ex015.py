print('{} DESAFIO 15 {}'.format(('='*5), ('='*5)))
dias = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos quilometros você rodou com o carro? '))
aluguel = (dias*60)+(km*0.15)
print('O preço a ser pego do aluguel será R${:.2f}'.format(aluguel))