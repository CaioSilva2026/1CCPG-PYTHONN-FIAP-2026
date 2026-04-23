cp = 0

while cp < 3:
    print(f"Produto {cp}")
    cp = cp + 1

# while decrescente
i = 4
while i >0:
    print(i)
    i -= 1

# repetição com entrada de usuário
jogar = "sim"

while jogar.lower() == "sim":
    print("Repete ou inicie o jogo")
    jogar = input("Deseja jogar novamente?")

# Modificadores de Laço break - continue

i = 0

while i < 10:
    i += 1

    if i == 3:
        continue

    if i == 7:
        break

    print(f"Produto{i}")

