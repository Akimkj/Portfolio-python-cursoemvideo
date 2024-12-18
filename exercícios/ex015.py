import math

kmPercorridos = float(input("Km percorridos com o carro alugado: "))
quantDias = int(input("Dias do carro alugado: "))

precoTotal = (60 * quantDias) + (kmPercorridos * 0.15)

print(f"O preço total do aluguel é igual a R${math.trunc(precoTotal)}")