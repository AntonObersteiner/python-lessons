def find_first(List, element):
    for index in range(len(List)):
        if List[index] == element:
            return index
    #raise ValueError()

def find_nth(List, element, n = 1):
    counter = 0
    for index in range(len(List)):
        if List[index] == element:
            counter += 1
            if counter == n:
                return index
    #raise ValueError()
