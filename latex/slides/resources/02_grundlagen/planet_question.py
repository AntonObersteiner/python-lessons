dt = .1
class Planet(...):
    """
    Planet(mass, Vector(x, y)) -> a mass at a position
        vel: velocity (initially (0, 0))
    planet.update() -> move self by vel * dt
    planet.accel(acc) -> accelerate vel by acc * dt
    planet.attract(other) -> accelerate planet towards other
    some random bits of physics:
        vel += acc * dt
        pos += vel * dt
        acc = force / mass
        force = G * mass1 * mass2 / dist ** 2
    """

    def __init__(self, mass, pos):
        super(Planet, self).__init__(pos.x, pos.y)
        ...
    def update(self): ...
    def accel(self, acc): ...
    def attract(self, other): ...
