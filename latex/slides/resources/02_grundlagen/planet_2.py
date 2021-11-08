    def attract(self, other):
        diff = self - other #__sub__
        dist = diff.abs()

        if dist > 0:
            force = self.mass * other.mass / dist ** 2
            factor = force / self.mass / dist
            directed_force = diff * factor #__mul__
            self.accel(directed_force)
