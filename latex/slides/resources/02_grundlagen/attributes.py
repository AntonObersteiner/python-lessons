class Mensch:
    def __init__(self, vorname, nachname):
        self.vorname = vorname
        self.nachname = nachname
    def vorstellen(self):
        return f"Hi, ich bin {self.vorname} {self.nachname}"

def main():
    # instanziiert zwei Objekte vom Typ 'Mensch'
    maria = Mensch("Maria", "Stuhlbein")
    john = Mensch("John", "Doe")
    print(maria.vorstellen())
