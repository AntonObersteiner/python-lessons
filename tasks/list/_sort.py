#!/usr/bin/env python3

def sort(List):
    """
    This is called bubble sort
    It's not that fast in general – but simple to understand
    Better sort algorithms are discussed in many Uni lectures
    """
    #tells us if the list is currently sorted
    sorted = False

    #only return when List is
    while not sorted:

        #we hope it is sorted,
        #   but we'll set this to False
        #   if we find out it's not
        might_be_sorted = True

        for i in range(0, len(List) - 1):
            if not List[i] <= List[i + 1]:
                List[i+1], List[i] = List[i], List[i+1]
                might_be_sorted = False
                #these two have been resorted, but it's not clear that the list is completely sorted

        #now we have checked through the list, we know for certain
        sorted = might_be_sorted

        #might_be_sorted and sorted can be the same variable,
        #   I write them as separate because I hope, it's easier to understand

    return List
