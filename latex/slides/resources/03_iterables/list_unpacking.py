students = [("Anastasia", True), ("Janneke", False)]

for student, present in students:
	if present:
		print(student + " is here")
	else:
		print(student + " is absent")
