def check(test_name, what_is, what_should_be):
    if what_is != what_should_be:
        filler = " " * len(test_name + ": ")

        print(f"{test_name}: Funktion ergibt: {what_is}")
        print(f"{filler}Sollte sein:     {what_should_be}")
    else:
        print(f"{test_name} passed! :)")


def check_error(test_name, func, args, error_type):
    filler = " " * len(test_name + ": ")

    try:
        result = func(*args)

        print(f"{test_name}: Funktion ergibt: {result}")
        print(f"{filler}Sollte Fehler werfen: {error_type}")
    except Exception as e:
        if isinstance(e, error_type):
            print(f"{test_name} passed! :)")
        else:
            print(f"{test_name}: Funktion wirft: {type(e)} '{e}'")
            print(f"{filler}Sollte werfen: {error_type}")
