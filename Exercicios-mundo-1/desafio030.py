#Um programa que lê um número e fala se ele é par ou impar

n = int((input("Digite um número inteiro... ")))
r = n % 2

if r == 0:
    print(" O número {} é par!".format(n))
else:
    print("O número {} é impar!".format(n))