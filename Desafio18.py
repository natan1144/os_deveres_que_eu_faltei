# Importação da biblioteca math
import math

# Definição da função que calcula o dobro, o triplo e a raíz quadrada de um número
def dobro_triplo_raiz(num):
    # Calcula o dobro, o triplo e a raíz quadrada de um número
    num_dobro = 2*num
    num_triplo = 3*num
    num_raiz = math.sqrt(num)
    # Imprime os valores descobertos
    print(f'O dobro de {num} é {num_dobro}.')
    print(f'O triplo de {num} é {num_triplo}.')
    print(f'A raíz quadrada de {num} é {num_raiz}.')

# Pede ao usuário um número para executar a função
num1 = float(input('Digite um número: '))
dobro_triplo_raiz(num1)


