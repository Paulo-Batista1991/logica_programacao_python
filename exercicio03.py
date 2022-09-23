"""Exemplo de aplicação 3: Elabore um programa que concatene tuplas."""

endereco_puc = ("Rua Imaculada Conceição", 1555, "Prado Velho", "Curitiba", "PR")
print(id(endereco_puc))
endereco_puc += ("Brasil",)
print(endereco_puc)
print(id(endereco_puc))