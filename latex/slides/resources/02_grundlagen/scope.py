var = 12
def foo():
    var = 9
    print(f"  in foo: {var}")

#def main...
print(f" vor foo: {var}")
foo()
print(f"nach foo: {var}")
