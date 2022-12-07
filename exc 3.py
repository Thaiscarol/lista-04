"""Faça um algoritimo para imprimir a soma dos  numeros entre um intervalo determinado pelo usúario, incluindo os limites inferiores e superiores. """


n1 = float(input("Digite o primeiro número do intervalo: "))
n2 = float(input("Digite o último número do intervalo: "))

soma= 0

while n1 <= n2:
    soma= soma+n1
    n1+=1

print("A soma total foi de :", soma)

