# aula 3 - 13.10.2020
# lista zero
# entrada de dados

dados = []
int1 = []
int2 = []
int3 = []
int4 = []
n = 0

while n >= 0:
  n = int(input("Digite um número:"))
  dados.append(n)
  if (0<=n<=25):
    int1.append(n) 
  elif (26<=n<=50):
    int2.append(n)
  elif (51<=n<=75):
    int3.append(n)
  elif (76<=n<=10):
    int4.append(n)
else:
  dados.pop()
  print("Fim da entrada de dados")


print(*dados)
print(f"Existem {len(int1)} números no intervalo de [0-25]")
print(f"Existem {len(int2)} números no intervalo de [26-50]")
print(f"Existem {len(int3)} números no intervalo de [51-75]")
print(f"Existem {len(int4)} números no intervalo de [76-100]")
