# Converter de metros para pés, polegadas e milhas

metros = float(input("Digite o valor em metros: "))
pes = metros * 3.28084

polegadas = metros * 39.3701
milhas = metros * 0.000621371

print(f"{metros} metros é igual a {pes:.2f} pés, {polegadas:.2f} polegadas e {milhas:.6f} milhas.")