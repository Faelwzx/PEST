n = int(input("digite um número: "))

soma = 0

for i in range(0, n+1, 1):
    soma += i

media = soma / (n + 1)
print(f"a média é: {media}")
