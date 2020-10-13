# aula 3 - 13.10.2020
# lista zero
# número primo
def calculaPrimo():
  num = int(input("Digite um número: "))


  if (num == 2):
    return(f"Número {num} é o único primo par")

  elif(num%2 ==0):
    return(f"Número {num} não é primo")

  for i in range(3,num):
    if num%i == 0:
      return((f"Número {num} não é primo"))

  return((f"Número {num} é primo"))
print(calculaPrimo())
