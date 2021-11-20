#!/usr/bin/env python3
from Vector import Vector
class Planet(Vector):
    """
    Planet(mass, Vector(x, y)) -> a mass at a position
        vel: velocity (initially (0, 0))
    planet.update(dt) -> move (dt is the timestep)
    planet.accel(acc, dt) -> accelerate (change vel by acc)
    planet.attract(other, dt) -> accelerate planet towards other
    """

    def __init__(self, mass, pos, vel = Vector(0, 0)):
        super(Planet, self).__init__(pos.x, pos.y)
        self.mass = mass
        self.vel = vel.copy()
    def __repr__(self):
        return f"P[{self.mass}]@{super().__str__()}"
    def __str__(self):
        return repr(self)

    def update(self, dt = .1):
        self += self.vel * dt
    def update_draw(self, turtle, dt = .1):
        turtle.pu() #pen up
        turtle.goto(self)
        self.update(dt)
        turtle.pd() #pen down
        turtle.goto(self)

    def accel(self, force, dt = .1):
        self.vel += force * (dt / self.mass)
    def attract(self, other, dt = .1, g = 100):
        diff = other - self
        dist = abs(diff)

        if dist > 0:
            force = g * self.mass * other.mass / dist ** 2
            factor = force / dist
            directed_force = diff * factor
            self.accel(dt, directed_force)

def main():
    #setting up the turtle to be fast
    import turtle
    turtle.delay(0)
    turtle.speed(0)
    turtle.ht()
    turtle.tracer(0, 0)

    A = Planet(20, Vector(100, 0), Vector(.01, 10))
    B = Planet(20, Vector(-100, 0), Vector(0, -10))
    C = Planet(100, Vector(0, 0), Vector(0, 0))

    dt = .1
    version = 0

    if version == 0:
        A = Planet(20,  Vector( 100,    0), Vector(.01,  -5))
        B = Planet(30,  Vector(-100,    0), Vector(  0,   5))
        C = Planet(50,  Vector(   0,    0), Vector(  0,   0))
        dt = .19
    elif version == 5:
        A = Planet(20,  Vector( 100,    0), Vector(.01,  10))
        B = Planet(20,  Vector(-100,    0), Vector(  0, -10))
        C = Planet(100, Vector(   0,    0), Vector(  0,   0))
        dt = .5
    elif version == 4:
        A = Planet(20,  Vector( 100,    0), Vector(  0,  10.25))
        B = Planet(20,  Vector(-100,    0), Vector(  0, -10.25))
        C = Planet(100, Vector(   0,    0), Vector(  0,   0))
    elif version == 1:
        A = Planet(20,  Vector( 100,  100), Vector(  2,  -1))
        B = Planet(100, Vector(-100, -100), Vector(  0,  .5))
        C = Planet(30,  Vector(  50,    0), Vector(  0,   0))
    elif version == 2:
        A = Planet(20,  Vector( 100,  100), Vector(  2,  -1))
        B = Planet(100, Vector(-100, -100), Vector(  0,  .1))
        C = Planet(30,  Vector(  50,    0), Vector(  0,   0))
    elif version == 3:
        A = Planet(20,  Vector( 100,  100), Vector(  2,  -1))
        B = Planet(100, Vector(-100, -100), Vector(  0,  .1))
        C = Planet(30,  Vector(  50,    0), Vector(  0,   0))
        dt = .2
    #Gesamt-Impuls = 0
    pA = A.vel * A.mass
    pB = B.vel * B.mass
    C.vel = (pA + pB) / C.mass

    while True:
        A.attract(B, dt)
        A.attract(C, dt)
        B.attract(A, dt)
        B.attract(C, dt)
        C.attract(A, dt)
        C.attract(B, dt)

        A.update_draw(turtle, dt)
        B.update_draw(turtle, dt)
        C.update_draw(turtle, dt)

        turtle.update()

if __name__ == '__main__':
    main()
