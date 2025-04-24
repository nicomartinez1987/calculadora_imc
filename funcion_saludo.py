def calcular_imc(peso, altura):
	imc = peso / (altura ** 2)
	print(f" tu IMC es: {imc:.2f}")

peso = float(input(" cuanto pesas? (en kg:"))
altura = float(input(" cuanto medis? (en metros:"))

calcular_imc( 75, 1.65)
