

# 1.Escreva um programa que soma dois números inteiros inseridos pelo usuário.
numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite outro número: "))
resultado = numero_1 + numero_2
print("O Resultado é : ", resultado)


# 2.Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

numero_1 = int(input("Digite um número: "))
resultado = numero_1 % 5
print("O Resultado é : ", resultado)




# 3.Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite outro número: "))
resultado = numero_1 * numero_2
print("O Resultado é : ", resultado)



# 4.Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

numero_1=  int(input("Digite um número: "))
numero_2 = int(input("Digite outro número "))
resultado = numero_1//numero_2
print(f" O Resultado é :",  resultado)


# 5.Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero_1 =  int(input("Digite um número: "))
resultado = numero_1 ** 2
print(f" O Resultado é :",  resultado)


# 6.Escreva um programa que receba dois números flutuantes e realize sua adição
numero_1 = float(input("Digite um numero: "))
numero_2 = float(input("Digite outro numero: "))
resultado = numero_1 + numero_2
print("O resultado é : ", resultado)

# 7.Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
numero_1 = float(input("Digite um numero: "))
numero_2 = float(input("Digite outro numero: "))
resultado = (numero_1 + numero_2)/2
print("O resultado é : ", resultado)


# 8.Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input("Digite um numero: "))
expoente  = float(input("Digite outro numero: "))
resultado = base ** expoente
print("O resultado é : " , resultado)

# 9.Faça um programa que converta a temperatura de Celsius para Fahrenheit.
temperatura_celsius = float(input("Digite a temperatura: "))
conversao = (temperatura_celsius * 1.8 +32)
print(" O resultado é : ", conversao)


# 10.Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio  = float(input("Digite o raio do círculo: "))
resultado = 3.14159265359 * (raio)**2
print(" O resultado é : ", resultado)

# 11.Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
nome = input("Escreva um nome: ")
resultado = nome.upper()
print(" O resultado é : ", resultado)



# 12.Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome_completo = input("Digite seu nome completo : ")
resultado = nome_completo.lower()
print("O Resultado é : ", resultado)