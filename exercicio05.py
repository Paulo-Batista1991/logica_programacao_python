"""Exemplo de aplicação 5:
Elabore um programa que faça uso de uma tupla chamada Endereco, contendo dados nomeados"""
.
from collections import namedtuple

Endereco = namedtuple("Endereco", ["logradouro", "numero", "bairro", "cidade", "estado"])
endereco_puc = Endereco(logradouro="Rua Imaculada Conceição", numero=1555, bairro="Prado Velho", cidade="Curitiba",
                        estado="PR")
print(f"Endereço: {endereco_puc[0]}")
print(f"  Número: {endereco_puc.numero}")
print(f"  Bairro: {endereco_puc.bairro}")
print(f"  Cidade: {endereco_puc.cidade}")
print(f"  Estado: {endereco_puc.estado}")