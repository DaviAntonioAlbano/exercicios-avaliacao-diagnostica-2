nome = input("Digite seu nome: ") 
anonascimento = input("Digite o ano de nascimento")
anoatual = input("Digite o ano atual : ")

idade = (anoatual - anonascimento)

if (idade >= 18):
	print("Você é maior e pode fazer a carteira de motorista")
elif (idade < 18 and idade >= 16):
	print("Você já pode votar")
	