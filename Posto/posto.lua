print("Digite o tipo de combustivel | g - Gasolina ; a - Alcool")
fuel = io.read()
print("Digite a quantidade em litros")
amount = math.tointeger(io.read())

if fuel == "a" then
	if amount > 20 then
		price = amount * 2.75
	else
		price = amount * 2.81
	end
	print(price)
end

if fuel == "g" then
	if amount > 20 then
		price = amount * 3.1
	else
		price = amount * 3.18
	end
	print(price)
end