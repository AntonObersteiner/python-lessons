var = 12
def foo():
    global var
    var = 9

#def main...
print(f"vor  foo: {var}")
foo()
print(f"nach foo: {var}")
