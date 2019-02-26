colors = ['red','blue','green','yellow']
for color in colors: print(color)

total_count=0
for color in colors:
	count = colors.index(color)+1
	total_count += count 
	print(str(count) + " " +color)
print("\nTotal Count = " + str(total_count))

numbers = list(range(1,6))
print(numbers)
#make even and odd lists
even_numbers = list(range(2,11,2))
odd_numbers = list(range(1,11,2))
print(even_numbers, odd_numbers)
#make a list of all square numbers
squares = []
for value in range(1,10):
	square = value**2
	squares.append(square)
	#should refactor squares.append(value**2)
print(squares)
#list comprehension can be used to simplify even further 
#*READ for every value in range take that value and ... then assign result to squares[], last index
squares = [value**2 for value in range(1,10)]
print(squares)
#splice a list
number_list = [value for value in range(0,100)]
print(number_list[5:11])
#omit start runs from index 0
print(number_list[:11])
#omit end runs until last index
print(number_list[95:])



