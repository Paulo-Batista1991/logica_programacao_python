"Elabore um programa que solicite ao usuário"
"o cadastro de endereços para entrega de produtos de uma loja."

endereco = []
print("Cadastro de Endereço de Entrega. ")
while True:
    logradoro = input("Digital o logradouro")
    numero = int(input("Digite o numero: "))
    bairro = input("Digite o bairro: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")
    novo_endereco = (logradoro, numero, bairro, cidade, estado)
    endereco.append(novo_endereco)
    if input("Deseja cadastrar um novo endereço (s/n): ") == "n":
        break
print("Os endereços cadastrados são: ")
for i in range(0, len(endereco)):
    endereco = endereco[i]
    print(f"{i}. {endereco[0]}, {endereco[1]}, {endereco[2]} - {endereco[3]}/{endereco[4]}")