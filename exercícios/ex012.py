preco = float(input("Digite o preço do produto: R$"))

novoPreco = preco - (preco * 5/100)

print(f"O novo valor do produto com 5% de desconto é de R${novoPreco:.2F}")