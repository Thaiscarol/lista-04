"""Faça um algoritimo que imprima os numeros de 1 até um numero especificado pelo usuario e a soma deles."""


n = float(input("Digite um numero:"))
a =1
soma = 0

while a <= n:
    soma = soma + a
    print(a)
    a+=1


print( " A soma de 1 até o numero que você digitou foi :",soma)