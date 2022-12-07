"""Faça um algoritimo para um intervalo de números informados pelo usuário e calcular, para cada  número , a raiz quadrada e sua metade. """

import math

n1 =int(input("Digite o primeiro número do intervalo:"))
n2 = int(input("Digite o´último numero do intervalo :"))

while n1<= n2:
    r = math.sqrt(n1)
    metade = n1/2
    print( " A raiz de ",n1,"é :",r, "e a metade no numero é: ", metade)
    n1+=1