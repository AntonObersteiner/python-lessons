try:
    #int(...) can fail
    #example: int("text") raises TypeError
    a = int(input("Give me an integer: "))
    print(f"Nice, you gave me {a}")
except TypeError:
    print("You didn't give an integer :(")
