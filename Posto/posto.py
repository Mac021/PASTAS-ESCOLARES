print("Type the kind of fuel | g - Gasoline ; a - Alcohol : ")
fuel = input()
print("Type the amount of it : ")
amount = float(input())

if fuel == "a":
	if amount > 20 :
		price = amount * 2.75
	else:
		price = amount * 2.81
	print("Final price is equal to")
	print(price)

if fuel == "g":
	if amount > 20 :
		price = amount * 3.1
	else:
		price = amount * 3.18
	print("Final price is equal to")
	print(price)
