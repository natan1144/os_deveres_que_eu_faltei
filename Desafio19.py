# Definição da função que calcula o perímetro
def perimetro_retangulo():
    # Pede ao usuário que informe a altura e o comprimento
    alt = float(input('Digite a altura do retângulo: '))
    comp = float(input('Digite o comprimento do retângulo: '))
    # Calcula o perímetro
    perimetro = 2*comp+2*alt
    # Imprime o perímetro do retângulo
    print(f'O perímetro do retângulo é igual à: {perimetro}')
    
# Execução da função
perimetro_retangulo()