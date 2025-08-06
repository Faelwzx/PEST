##Livro com desconto

livro = float(input("digite o numero de livros:"))

capa = 24,95
desconto = capa * 0.40

transporte = 3.00
adicional = 0.75 * capa
preco_final = capa - desconto + transporte + adicional

print(f"O preço final do livro é: {preco_final:.2f}")