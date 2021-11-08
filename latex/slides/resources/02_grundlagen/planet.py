class Planet(...):
    """
    Planet(mass, Vector(x, y)) -> a mass at a position
        vel: velocity (initially (0, 0))
    planet.update(dt) -> move (dt is the timestep)
    planet.accel(dt, acc) -> accelerate (change vel by acc)
    planet.attract(other) -> accelerate planet towards other
    """

    def __init__(self, mass, pos):
        super(Planet, self).__init__(pos.x, pos.y)
        self.mass = mass
    def update(self, dt):
        self.add(self.vel.mul(dt))
    def accel(self, dt, acc):
        self.vel.add(add.mul(dt))
