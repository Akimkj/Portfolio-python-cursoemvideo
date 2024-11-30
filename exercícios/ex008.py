num = float(input("Digite uma distância em metros: "))
mm = num * 1000
cm = num * 100
dm = num * 10
dam = num / 10
hm = num / 100
km = num /1000
print(f"A medida de {num}m corresponde a: ")
print(f"{km}km -- {hm}hm -- {dam}dam -- {dm}dm -- {cm}cm -- {mm}mm")
