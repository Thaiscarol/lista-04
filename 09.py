"""Faça um algoritimo para calcular o cubo e quadrado de todos os números pertencentes a um intervalo, incluido o limite superior e inferior. """


n1 = int(input(" Digite o primeiro número do intervalo: "))
n2 = int(input( "Digite o segundo número do intervalo"))

while n1 <= n2:
    cubo = n1** 3
    q = n1** 2
    print("O cubo de ",n1,"é ",cubo, "e o quadrado é: ",q)
    n1+= 1