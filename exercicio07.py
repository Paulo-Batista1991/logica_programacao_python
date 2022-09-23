"""Exemplo de aplicação 7: Elabore um programa que simule o cadastro de telefones com
dicionário como uma agenda. Caso seja informado um nome já existente, deve perguntar se
deseja alterar os dados existentes. Caso seja um telefone já existente, deve informar que
esse telefone já está cadastrado em outro contato, não podendo ser efetuada a inclusão.
 Ao final, deve exibir o dicionário."""

agenda = {}
print("*** Cadastro de telefone ***")
while True:
    contato = input("Digite o nome de contato: ")
    telefone = input("Digite o telefone do contato: ")
    if contato in agenda:
        if input(f"Contato já cadastrado com número com o númeoro{agenda[contato]}. Deseja alterar (s/n)") == "n":
            continue
    if telefone in agenda.values():
        print("Telefone já é cadastrado para outro contato ")
        continue
    agenda[contato] = telefone
    if input("Deseja cadastrar um nono contato (s/n): ") == "n":
        break
    print(agenda)
