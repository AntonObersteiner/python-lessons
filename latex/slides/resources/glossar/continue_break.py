for i in range(10, 101, 10):
	if i == 30:
		#program continues with 40 -> no 30 in print
		continue
	print(f"{i}% done!")
	if i == 90:
		#90% will be printed, then this message, then it will exit
		print("At 90%, there's a problem, no next loop")
		break
		#no 100% :/
