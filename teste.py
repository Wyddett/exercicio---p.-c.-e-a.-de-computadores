from main import listar_lista, media_lista, maior_numero_lista, menor_numero_lista, quantidade_numeros_pares

print("Olá usuário, tudo bem?", end="\n\n")

print(f"Lista: {listar_lista()}", end="\n\n")

print("OPÇÕES: ")
print("1. Média da lista")
print("2. Maior número da lista")
print("3. Menor número da lista")
print("4. Números pares da lista")
print("5. Encerrar programa")


while True:
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        print(f"Média: {media_lista()}", end="\n\n")
    elif opcao == 2:
        print(f"Maior número: {maior_numero_lista()}", end="\n\n")
    elif opcao == 3:
        print(f"Menor número: {menor_numero_lista()}", end="\n\n")
    elif opcao == 4:
        print(f"Quantidade de números pares: {quantidade_numeros_pares()}", end="\n\n")
    elif opcao == 5:
        print("Programa encerrado")
        break