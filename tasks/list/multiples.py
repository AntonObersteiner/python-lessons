#!/usr/bin/env python3

"""
Die Funktion remove_multiples(Liste, factor) löscht
    alle Vielfachen (element % factor == 0) und gibt die Liste zurück.
"""

def remove_multiples(Liste, factor):
    #Was sind verschiedene Probleme von:
    #Liste.remove(elemet)
    #Liste.pop(index)

    return Liste

"""
Hier wird geprüft, ob die Funktion tut, was sie soll
"""
from check import check
def test():
    print("Testing:")

    check("aus [1,2,3,6,7,8,9] die Vielfachen von 3:", remove_multiples([1, 2, 3, 6, 7, 8, 9], 3), [1, 2, 7, 8])

if __name__ == '__main__':
    test()
