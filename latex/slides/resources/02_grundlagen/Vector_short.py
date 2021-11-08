class Vector:
    def __init__(self, x, y): <...>
    def __add__( self, other):        #self + other
        return Vector( <...> )
    def __iadd__(self, other):        #self += other
        self.x += other.x
        self.y += other.y
        return self
    def __sub__( self, other):  <...> #self - other
    def __isub__(self, other):  <...> #self -= other
    def __mul__( self, factor): <...> #self * factor
    def __imul__(self, factor): <...> #self *= factor
    def __abs__( self): <...>         #abs(self)
    def __iter__(self): <...>         #<...>
