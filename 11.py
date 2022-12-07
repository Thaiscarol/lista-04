"""Faça um algoritimo para ler 100 numeros,calcular a soma dos numeros, a media  e o maior e menor numero encontrados."""


a = 1
b =6
soma = 0
maior = 0
menor = 11111111111111111

while a < b:
    n= int(input( "Digite um número :"))
    soma = soma + n
    media = soma/5
    if n > maior :
        maior = n
    if n < menor:
        menor = n
    a+=1

print( " A soma de todos os numeros foi de :",soma)
print("A média dos números foi de: ", media)
print("o maior número digitado foi: ", maior)
print( "O menor número digitado foi ", menor)