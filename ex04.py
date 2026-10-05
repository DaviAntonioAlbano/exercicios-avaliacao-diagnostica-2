#F.U.P para informar 10 números e no final, mostrar a quanƟdade de números pares, a quanƟdade de números ímpares, a soma dos números pares e a soma dos números ímpares.

pares = 0
impares = 0
soma_pares = 0
soma_impares = 0

for i in range(10):
    numero = float(input("Digite um número: "))
    if numero % 2 == 0:
        pares += 1
        soma_pares += numero
    else:
        impares += 1
        soma_impares += numero

print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)
print("Soma dos números pares:", soma_pares)
print("Soma dos números ímpares:", soma_impares)