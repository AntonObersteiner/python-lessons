content = []
file1 = open("Source.txt", "r") #r = read
for line in file1:
	content += [line]
file1.close()

file2 = open("Result.txt", "w") #w = write
for l in range(len(content)):
	file2.write(f"{l:03}: {content[l]}")
file2.close()
