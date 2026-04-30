lista_frutas = ["Banana", "Maçã", "Morango"]

# Listas de frutas[0] = "Banana"
# Listas de frutas[1] = "Maçã"
# Listas de frutas[2] = "Morango"
print(lista_frutas[1:3])

lista_frutas.append("Pera")
print(lista_frutas)

qtd_frutas = len(lista_frutas)
print("Qtd de frutas ", qtd_frutas)

#FOR INDEXADO para PERCORRER
for i in range(qtd_frutas):
    print(lista_frutas[i])

print()

#FOR EACH em python
for fruta in lista_frutas:
    print(fruta)

numeros = [0, 5, 11, 4]
for numeros in numeros:
    print(numeros)