#  F.U.P para informar idade e nome de pessoas. São 5 pessoas.

pessoa_mais_velha = ""
idade_mais_velha = 0

for i in range(5):

    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    
    if idade > idade_mais_velha:
        idade_mais_velha = idade
        pessoa_mais_velha = nome

print("A pessoa mais velha é:", pessoa_mais_velha)
print("Sua idade é:", idade_mais_velha)