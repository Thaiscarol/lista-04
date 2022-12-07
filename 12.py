"""Faça um algoritimo para calcular a media de n numero informados pelo usuario. Para sair do calculo, o usuario deverá digitar um numero negativo  """


soma = 0
a = 1
cont = 1

while a > 0:
    n = int(input("Digite um número :"))
    if n > 0:
        soma = soma +n
        media = soma/ cont
        cont +=1
    else:
        a = -1


print(" A média dos numeros digitados foi de :", media)
print( "Fim do programa !")