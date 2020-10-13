# aula 3 - 13.10.2020
# lista zero
# tabuada

n = int(input("Montar a tabuada de: "))
c = int(input("Começar em: "))
f = int(input("Finalizar em: "))
num = []


for i in range(c, f+1):
  num.append(i)

for i in num:
  print(f"{i} X {n} = {i*int(n)}")
