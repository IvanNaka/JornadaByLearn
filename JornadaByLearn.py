# Ivan Yudi Oda Nakatani 07/01/2020
primeironumero = int(input('Coloque o primeiro número: '))
segundonumero = int(input('Coloque o segundo número: '))
conta = str(input('Qual operação deseja fazer? '))
soma = primeironumero + segundonumero
subtracao = primeironumero - segundonumero
multiplicacao = primeironumero * segundonumero
divisao = primeironumero / segundonumero
media = (primeironumero + segundonumero) / 2

if conta == 'soma':
  print(f'A soma é {soma} ')
elif conta == 'subtração':
  print(f'A subtração é {subtracao} ')
elif conta == 'multiplicação':
  print(f'A multiplicão é {multiplicacao}')
elif conta == 'divisão':
  print(f'A divisão é {divisao}')
elif conta == 'média':
  print(f'A média é {media}')
else:
 print('Não entendi a operação') 

