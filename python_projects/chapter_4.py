colors = ['red','blue','green','yellow']
for color in colors: print(color)

total_count=0
for color in colors:
	count = colors.index(color)+1
	total_count += count 
	print(str(count) + " " +color)
print("\nTotal Count = " + str(total_count))
