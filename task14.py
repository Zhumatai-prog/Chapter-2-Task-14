numbers = input("Enter a list of numbers: ")
number = list(numbers)
for i in number:
	if i % 2 == 0:
		print (i)
	else:
		continue