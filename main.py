lista = [10, 23, 5, 8, 12, 33, 42, 7, 19, 28, 3, 16, 9, 50, 21]

def listar_lista():
    return lista

def media_lista():
    soma = 0

    for i in range(0, len(lista)-1):
        soma = soma + lista[i]
        i = i + 1

    media = round(soma / len(lista), 2)
    return media

def maior_numero_lista():
    maior_numero = 0

    for i in range(0, len(lista)-1):
        if lista[i] > maior_numero:
            maior_numero = lista[i]

    return maior_numero

def menor_numero_lista():
    menor_numero = 999

    for i in range(0, len(lista)-1):
        if lista[i] < menor_numero:
            menor_numero = lista[i]

    return menor_numero

def quantidade_numeros_pares():
    quantidade_numeros_pares = 0
    for i in range(0, len(lista)-1):
        if lista[i] % 2 == 0:
            quantidade_numeros_pares = quantidade_numeros_pares + lista[i]

    return quantidade_numeros_pares