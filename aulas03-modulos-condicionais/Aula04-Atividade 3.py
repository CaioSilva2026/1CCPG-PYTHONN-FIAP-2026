qtd_produtos = int(input("Digite a qtd. de produtos: "))

for i in range(qtd_produtos):
    print(f"Produto {i+1}")

    for i in range(0 ,4):
        for j in range(0, 3, 2):
            print(f"i: {i}, j:{j}")