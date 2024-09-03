'''receba 3 numeros e verifique se o primeiro é maior que o segundo mas menor q o terceiro'''
num1 = input('\nQual seu primeiro número: ')
num2 = input('\nQual seu segundo número: ')
num3 = input('\nQual seu terceiro número: ')
num1 = float(num1)
num2 = float(num2)
num3 = float(num3)

'''fazendo a comparaçao dos numeros para exibir o devido resultado'''
if num1 > num2 and num1 < num3:
    print(f'{num1} é maior q {num2} e menor que {num3}')
elif num1 > num2 and num1 > num3:
    print(f'{num1} é maior q {num2} e maior que {num3}')
else:
    print(f'{num1} é menor q {num2} e {num3}')