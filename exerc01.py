"""Exercício de fixação 1: Crie um programa que efetue o cadastro de pessoas com nome, RG e CPF
por meio de tuplas, adicionando-as a uma lista e imprimindo essa lista no fim do programa."""

pessoas =[]
while True:
    nome = input("Digite seu nome: ")
    rg = int(input("Digite seu RG: "))
    cpf = int(input("Digite seu CPF: "))
    pessoa = (nome, rg, cpf)
    pessoas.append(pessoa)
    if input("Gostaria de cadastrar mais um pessoa (s/n)") == "n":
        break
print(pessoa)