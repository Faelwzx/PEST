# Programa para calcular a soma dos dígitos de um número de 4 dígitos

numero = int(input("Digite um número de 4 dígitos: "))

if 1000 <= numero <= 9999:
    digito1 = numero // 1000
    digito2 = (numero // 100) % 10
    digito3 = (numero // 10) % 10
    digito4 = numero % 10

    soma_digitos = digito1 + digito2 + digito3 + digito4

    print(f"A soma dos dígitos do número {numero} é: {soma_digitos}")