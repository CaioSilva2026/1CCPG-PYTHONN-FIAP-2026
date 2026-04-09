from operator import truediv

num1 = 4
num2 = 2

operacao = num1 / num2
print(operacao, type(operacao))

# operadores de atribuicao

num = 15
print() # pular linha
print(num)

num = num + 2
print(num)

num /= 2
print (num)
# operadores relacionais
print()
print(6 >= 6)

idade = 20

print(idade >= 21)

logado = True
print(logado, type(logado))

maior_idade = idade >= 18
print(maior_idade)

#STRINGS

nome1 = "Marcos"
nome2 = "marcos"

print(nome1.upper() == nome2) #upper vai garantir que todos ficam MAIUSCULO
