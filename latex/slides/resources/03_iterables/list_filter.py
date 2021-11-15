max_n = 1000

numbers = list(range(2, max_n))
for p in range(2, int(max_n ** .5)):
	if p in numbers:
		numbers = list(filter(
			#welche n behalten?
			lambda n:
				n == p  or
				n % p != 0,
				# % == mod
			numbers
		))

print(numbers)
