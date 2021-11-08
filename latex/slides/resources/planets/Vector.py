#!/usr/bin/env python3
class Vector:
    """
    A Vector(x, y) has the attributes x and y.
    defined operators: +, +=, -, -=, *, *=
    defined functions: str(), repr(), self.copy(), abs(), len() = 2
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        #   x, y   converts to tuple and that is printed as (x, y)
        return f"{self.x, self.y}"
    def __repr__(self):
        return f"V{self.x, self.y}"
    def copy(self):
        """return a copy of the object"""
        return Vector(self.x, self.y)
    def __add__(self, other):
        """called for self + other"""
        return Vector(
            self.x + other.x,
            self.y + other.y,
        )
    def __iadd__(self, other):
        """called for self += other, return self!"""
        self.x += other.x
        self.y += other.y
        return self
    def __sub__(self, other):
        """called for self + other"""
        return Vector(
            self.x - other.x,
            self.y - other.y,
        )
    def __isub__(self, other):
        """called for self += other, return self!"""
        self.x -= other.x
        self.y -= other.y
        return self
    def __mul__(self, factor):
        """called for self * factor"""
        return Vector(
            self.x * factor,
            self.y * factor,
        )
    def __rmul__(self, factor):
        """called for factor * self"""
        return self * factor
    def __imul__(self, factor):
        """called for self *= factor, return self!"""
        self.x *= factor
        self.y *= factor
        return self
    def __truediv__(self, divisor):
        """called for self / divisor"""
        return Vector(
            self.x / divisor,
            self.y / divisor,
        )
    def __itruediv__(self, divisor):
        """called for self /= divisor"""
        self.x /= divisor
        self.y /= divisor
        return self
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** .5
    def __iter__(self):
        """called for converting to lists, tuples
        used in for-loops and many other cases"""
        yield self.x
        yield self.y
    def __len__(self):
        return 2

def main():
    a = Vector(1, 2)
    b = Vector(3, 4)
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"a - b: {a + b}")
    c = a + b
    print(f"c = a + b: {c}")
    print(f"c / 2: {c / 2}")
    b *= 3
    print(f"b *= 3: {b}")
    c += b
    print(f"c += b: {c}")
    c -= b * .5
    print(f"c -= b * .5: {c}")
    print(f"abs(a): {abs(a)}")
    d = c.copy()
    print(f"d = copy(c): {d}")
    d += a
    print(f"d += a != c: {d} != {c}")
    print(f"len(d): {len(d)}")

if __name__ == '__main__':
    main()
