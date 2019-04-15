def func(n):
	if n%2==0:
		return n
	else:
		return '{} is odd'.format(n)
		
number = int(input('Enter a number'))
print(func(number))