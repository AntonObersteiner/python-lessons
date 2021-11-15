from Vector import Vector
dt = .1 #time step per update
class Planet(Vector):
    """
    Planet(mass, Vector(x, y)) -> a mass at a position
        vel: velocity (initially (0, 0))
    planet.update() -> move (timestep: global dt)
    planet.accel(force) -> accelerate (vel by force/mass)
    planet.attract(other) -> accelerate planet towards other
    """

    def __init__(self, mass, pos):
        super(Planet, self).__init__(pos.x, pos.y)
        self.mass = mass
    def update(self):
        self += self.vel * dt #__iadd__, __mul__
    def accel(self, force):
        self.vel += force * (dt / self.mass)  #__iadd__, __mul__
