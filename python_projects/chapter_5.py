cars = ["bmw","honda","ford","chevy"]

for car in cars:
	if car == "bmw":
		print(car.upper())
	elif car == "ford": 
		print(car.title() + "'s are a POS")
	else:
		print(car.title())

#in list check
print("bmw" in cars)
print("audi" in cars)
#not in list check
car = "audi"
if car not in cars:
	print("You don't own an " + car.title())
