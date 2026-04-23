# Escreva um programa que dadas duas notas de 0 a 10
# Calcula a média aritimética entre elas.
def validar_nota(nota):
    nota_temp = nota
    while nota < 0 or nota > 10:
        print("A nota deve estar entre 0 e 10")
        nota_temp = float(input("Digite novamente a nota: "))
    return nota_temp


# solicitar e validar a primeira nota
notaA = float(input("Digite a primeira nota: "))
notaA = validar_nota(notaA)
# while notaA < 0 or notaA > 10:
  #  print("A nota deve estar entre 0 e 10")
 #   notaA = float(input("Digite novamente a primeira nota: "))

# solicitar e validar a segunda nota
notaB = float(input("Digite a segunda nota: "))
while notaB < 0 or notaB > 10:
    print("A nota deve estar entre 0 e 10")
    notaA = float(input("Digite novamente a segunda nota: "))

# Calcular a media

media = (notaA + notaB) / 2
print("A media é", media)