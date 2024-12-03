largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))
area = largura * altura
print(f"A sua parede tem a dimensão {largura} X {altura}. Logo, tem uma área igual a {area}m²")
litros = area / 2
print(f"Você vai precisar de {litros:.2F} litros de tinta para pintar a parede")