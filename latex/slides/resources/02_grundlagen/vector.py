class Vector:
    """
    Vector(x, y) -> an object with attributes x and y
    vec.add(vec2) -> vec + vec2
    vec.mul(factor) -> vec * factor
    vec.abs() -> (x**2 + y**2) ** .5
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, vec2):
        return Vector(self.x + vec2.x, self.y + vec2.y)
    def mul(self, factor):
        return Vector(self.x * factor, self.y * factor)
    def abs(self):
        return (self.x ** 2 + self.x ** 2) ** .5
