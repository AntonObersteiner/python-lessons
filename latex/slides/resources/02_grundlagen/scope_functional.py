var = 12
def foo(variable):
    variable = 9
    print(f"  in foo: {variable}")
    return variable

print(f" vor foo: {var}")
var = foo(var)
print(f"nach foo: {var}")
