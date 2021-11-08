var = 12
def foo(variable):
    variable = 9
    print(f"  in foo: {variable}")

#def main...
print(f" vor foo: {var}")
foo(var)
print(f"nach foo: {var}")
