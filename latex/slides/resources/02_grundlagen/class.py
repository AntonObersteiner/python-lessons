class Klasse:
    def __init__(self, wert):
        self.attribut = wert

    def print_attribut(self):
        print(self.attribut)

def main():
    a = Klasse(3)
    b = Klasse(12)
    a.attribut = -a.attribut
    b.print_attribut()
