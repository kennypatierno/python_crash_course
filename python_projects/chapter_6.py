fighter_0 = {
	'name':'Solid Snake',
	'height':66, 
	'rating':95
	} 

print(fighter_0['name'] + " is " + str(fighter_0['height']) + 
" inches tall and has a rating of " + str(fighter_0['rating']))
#append
fighter_0['speed']= 75
fighter_0['strength']=80
print(fighter_0)

fighter_1 = {}
print(fighter_1)

fighter_1['name']='Liquid Snake'
fighter_1['height']=66
fighter_1['rating']=88
fighter_1['speed']=90
fighter_1['strength']=75

print(str(fighter_1)+ "\n")
#nested dictionary; dictionary of dictionaries 
fighters={'Player One':fighter_0,'Player Two':fighter_1}
print(fighters)
#for loop
for key, value in fighter_0.items():
	#added this because some values are ints and cannot concat
	value = str(value)
	print("\nKey: " + key.title())
	print("Value: " + value)

#nested for loop
for key, value in fighters.items():
	for key, value in fighter_0.items():
		#added this because some values are ints and cannot concat
		vaalue = str(value)
		print("\nKey: " + key.title() + "|| Value: " + value)


