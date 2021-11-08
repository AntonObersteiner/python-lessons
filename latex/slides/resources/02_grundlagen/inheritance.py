class Mensch():
    def __init__(self, vorname, nachname):
        self.vorname = vorname
        self.nachname = nachname

class Kind(Mensch):
    def __init__(self, vorname, nachname, eltern):
        super.__init__(vorname, nachname)
        self.eltern = eltern
