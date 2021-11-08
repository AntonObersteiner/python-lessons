def say_hi(name, greet):
    return greet+", "+name

file = open("Datei.txt")
file.write(say_hi("Kurs"))
file.close()
