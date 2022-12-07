"""Elabore um algoritimo para calcular a soma dos numeros ímpares de 1000 a 10. """

n1 =1000
n2 = 10
soma = 0

while n1 <= n2:
    if n1%2 != 0:
        soma = soma+ n1
        n1+=1

print(" A soma dos números ímpares de 1000  a 10")