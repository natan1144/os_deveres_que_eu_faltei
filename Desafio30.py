'''exibir o numero absoluto do valor recebido'''
sinal = input('Digite (1) se seu numero for positivo ou (2) se ele for negativo: ')
num1 = float(input("Qual seu número?: "))

'''faz a comparação de sinais, para exibir o0 resultado'''
if (sinal == '1'):
    print(' ________________________________________________')
    print(f'| Como {num1} é positivo, seu ovalor absoluto é {num1} |')
    print('|________________________________________________|')
else:
    print(' ___________________________________________________________________')
    print(f'|Como -{num1} é negativo, seu valor absoluto é o oposto, logo será {num1} |')
    print('|___________________________________________________________________|')