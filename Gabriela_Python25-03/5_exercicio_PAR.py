import time

numero = int(input("Digite um número positivo:"))
while(numero < 0):
    numero = in(input("Digite um número positivo"))

if numero % 2 == 0:
    print(' "P-A-R!!"')
    
else:
    print("Tente outra vez...")