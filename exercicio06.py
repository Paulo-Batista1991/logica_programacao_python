"""Exemplo de aplicação 6: Elabore um programa que simule o cadastro de telefones com
dicionário como uma agenda, exibindo, ao final, o dicionário."""

agenda = {}
print("*** Cadastro de telefone ***")
while True:
    contato = input("Digite o nome do contato")
    telefone = input("Digite o telefone do contato: ")
    agenda[contato] =  telefone
    if input("Deseja cadastrar um novo conta(s/n): ") == "n":
        break
    print(agenda)