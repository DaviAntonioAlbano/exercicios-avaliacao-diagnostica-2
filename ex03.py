# F.U.P para informar 10 números e no final, mostrar o resultado da soma. Ex: Se for informado: 2, 4, 10.....Deverá somar esses números e mostrar o resultado. (Usar ofor).

soma = 0
for i in range(10):
    numero = float(input("Digite um número: "))
    soma += numero

print("A soma dos números digitados é: ", soma)