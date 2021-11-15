dt = .1 #time step
class Planet(...):
    """
    Planet(mass:float, Vector(x, y)) -> a mass at a position
        vel: velocity (initially (0, 0))
    planet.update() -> move self by vel * dt
    planet.accel(force) -> accelerate (vel by force / mass)
    planet.attract(other) -> accelerate planet towards other
    """

    def __init__(self, mass, pos):
        super(Planet, self).__init__(pos.x, pos.y)
        ...
    def update(self): ...
    def accel(self, force): ...
    def attract(self, other): ...
