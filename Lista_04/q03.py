num_fim = int(input("digite um número: "))

soma = 0

for i in range(0, num_fim+1, 2):
    soma += i
print(f"a soma é: {soma}")