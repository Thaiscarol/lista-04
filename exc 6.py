"""Elabore um algoritimo para calcular a soma dos números ímpares de 0 a 100."""

n1 =0
n2 =100
soma =0

while n1 <= n2 :
    if n1%2 !=0 :
        soma= soma + n1
        n1+=1

print(" A soma dos números ímpares de 0 a 100 foi de : ", soma)
