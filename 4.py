"""Faça um algoritimo para imprimir os multiplos de 5 em um intervalo informando pelo usuario"""

n1 = float(input("Digite o primeiro número do intervalo"))
n2 = float(input("Digite o último número do intervalo"))

while n1 <= n2:
    if (n1 % 5 == 0):
        print(n1)
        n1 += 1

