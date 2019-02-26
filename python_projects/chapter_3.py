cars = ["ford","dodge","chevy","honda"]
print(cars)
print(cars[0].title())
#return last item in any list
print(cars[-1].title())
#return SECOND to last item in any list...
print(cars[-2].title())

cars.append("oldsmobile")
message = "My first car was an " + cars[-1].title() + ". After that I got a shitty " + cars[0].title() + ". LOL"
print(message) 

shoes=[]
shoes.append("nike")
shoes.append("reebok")
shoes.append("puma")
print(shoes)

shoes.insert(0, "chucks")
print(shoes)

del shoes[-1]
print(shoes)
shoes.append("puma")
print(shoes)

popped_shoe = shoes.pop()
print(shoes)
print(popped_shoe)

shoes.append(popped_shoe)
print(shoes)

shoes.sort()
print(shoes)
shoes.sort(reverse=True)
print(shoes)

print(len(shoes))
