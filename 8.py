"""Faça um algoritimo para ler cinco números e imprimir o cubo e o quadrado de cada um deles"""

a = 1
b = 6

while a < b:
    n=int(input( " Digite um número :"))
    cubo = n**3
    q = n**2
    print("O cubo de ",n,"é: ",cubo, " e o quadrado é : ",q)
    a+=1