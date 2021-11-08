    def attract(self, dt, other):
        diff = Vector(
            other.x - self.x,
            other.y - self.y
        )
        dist = diff.abs()

        if dist > 0:
            force = self.mass * other.mass / dist ** 2
            factor = force / self.mass / diff.abs()
            directed_force = diff.mul(factor)
            self.accel(dt, directed_force)
