import math

catetoMenor = float(input("Digite o menor cateto: "))
catetoMaior = float(input("Digite o maior cateto: "))

hipotenusa = math.hypot(catetoMenor, catetoMaior)

print(hipotenusa)