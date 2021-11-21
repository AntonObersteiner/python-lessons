with open("Source.txt", "r") as file:
	l = 0
	for line in file:
		print(f"{l:03}: {line}")
		l += 1
