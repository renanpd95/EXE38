import os,math

r = int(input("Digite o valor do raio: "))
h = int(input("Digite o valor da altura: "))
os.system('clear')
pote = math.pow(r,2)
cilin = 3.14*pote*h

print ("O volume do cilindro é: ",cilin)


