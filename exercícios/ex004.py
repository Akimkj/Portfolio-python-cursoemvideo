conteudo = input("Digite qualquer coisa: ")

print(f"O tipo primitivo desse valor é {type(conteudo)}")
print(f"É só espaço? {conteudo.isspace()}")
print(f"É numérico? {conteudo.isnumeric()}")
print(f"É alfabético? {conteudo.isalpha()}")
print(f"É alfanumérico? {conteudo.isalnum()}")
print(f"Está em maiúsculas? {conteudo.isupper()}")
print(f"Está em minúscula? {conteudo.islower()}")
print(f"Está Capitalizada? {conteudo.istitle()}")