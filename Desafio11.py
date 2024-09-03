# Definição das funções de criar listas e dobrar os números das listas
def criar_lista(n_elementos):
    # Cria a lista números
    numeros = []
    # Pede n números e adicione eles na lista
    for _ in range(0,n_elementos):
        num = int(input('Digite um número: '))
        numeros.append(num)
    return numeros

def dobrar_numeros(lista):
    # Imprime a lista original
    print(f'Lista original: {lista}')
    # Cria a lista numeros_dobrados
    numeros_dobrados = []
    # Para cada elemento da lista fornecida, ele dobra o número e coloca na lista numeros_dobrados
    for n in lista:
        n *= 2
        numeros_dobrados.append(n)
    # Imprime a lista com os números dobrados
    print(f'Lista com os números dobrados: {numeros_dobrados}')


# Cria uma lista de 10 números e dobra cada um dos seus elementos
dobrar_numeros(criar_lista(10))
    