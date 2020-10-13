# aula 3 - 13.10.2020
# lista zero
# par ou impar

par = []
impar = []

for i in range(0, 4):
  n = int(input("Digite um número: "))
  if (n%2 == 0):
    par.append(n)
  else:
    impar.append(n)

print(f"Par: {par} e Impar: {impar}")
