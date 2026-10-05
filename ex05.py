#  F.U.P que calcule a média dos números digitados pelo usuário, se eles forem pares. Sendo que são 5 números. Para verificar se o número é par, usar o comando % (MOD) .

pares = 0
soma = 0

for i in range(5):

    numero = float(input("Digite um número: "))
    if numero % 2 == 0:
        pares += 1
        soma += numero
        media = soma / pares if pares > 0 else 0

print("A média dos números pares é: ", media)

