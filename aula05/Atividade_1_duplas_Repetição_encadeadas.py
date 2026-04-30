listas_de_nomes = ["Enzo", "joao", "josé", "Ana"]

for i in range(len(listas_de_nomes)):
    for qtd_pessoas in range(i + 1, len(listas_de_nomes)):
        print(listas_de_nomes[i], listas_de_nomes[qtd_pessoas])
print()