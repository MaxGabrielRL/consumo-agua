# solicitar o tipo de imóvel e converter para minúsculas
tipo = input("Digite o tipo de imóvel (comercial, casa ou apartamento): ").strip().lower()

# solicitar o consumo de água em m³
consumo = float(input("Digite o consumo mensal de água em m³: "))

# Classificação de acordo com as regras do negócio
if tipo == "comercial":
    print("Tarifa comercial aplicada - consulte o plano corporativo.")

elif tipo == "apartamento" and consumo < 10:
    print("Consumo econômico - excelente controle de água!")

elif tipo == "apartamento" or (tipo == "casa" and consumo <= 25):
    print("Consumo moderado - dentro do padrão residencial.")

else:
    print("Consumo excessivo - necessário economizar água e verificar possíveis vazamentos.")    