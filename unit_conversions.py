class Length(object):
    def __init__(self, length):
        self.length = length  # This is in the SI unit, meters

    def __add__(self, other):
        return Length.set_m(self.length + other.length)

    def __sub__(self, other):
        return Length.set_m(self.length - other.length)

    def get_m(self):  # meters
        return self.length

    @classmethod
    def set_m(cls, length):
        return cls(length)

    def get_inch(self):  # inches
        return self.length * 39.37008

    @classmethod
    def set_inch(cls, length):
        return cls(length / 39.37008)

    def get_ft(self):  # feet
        return self.length * 3.28084

    @classmethod
    def set_ft(self, value):
        return self(value / 3.28084)


class Speed(object):
    def __init__(self, speed):
        self.speed = speed  # This is in the SI unit, mps

    def __add__(self, other):
        return speed.set_mps(self.speed + other.speed)

    def __sub__(self, other):
        return speed.set_mps(self.speed - other.speed)

    def get_mps(self):  # meters per second
        return self.speed

    @classmethod
    def set_mps(cls, speed):
        return cls(speed)

    def get_inps(self):  # inches per second
        return self.speed * 39.37008

    @classmethod
    def set_inps(cls, speed):
        return cls(speed / 39.37008)

    def get_fps(self):  # feet per second
        return self.speed * 3.28084

    @classmethod
    def set_fps(self, value):
        return self(value / 3.28084)

    def get_miph(self):
        return self.speed * 2.236936

    @classmethod
    def set_miph(self, value):  # miles per hour
        return self(value / 2.236936)


class Weight(object):
    def __init__(self, weight):
        self.weight = weight  # In the SI unit, g

    @classmethod
    def set_g(cls, weight):
        return cls(weight)

    def get_g(self):
        return self.weight

    @classmethod
    def set_kg(cls, weight):
        return cls(weight * 1000)

    def get_kg(self):
        return self.weight / 1000

    @classmethod
    def set_lb(cls, weight):
        return cls(weight * 453.5924)

    def get_lb(self):
        return self.weight / 453.5924

    def __add__(self, other):
        return Weight.set_kg(self.get_kg() + other.get_kg())


class Force(object):
    def __init__(self, force):
        self.force = force  # In the SI unit, g

    @classmethod
    def set_N(cls, force):
        return cls(force)

    def get_N(self):
        return self.force

    @classmethod
    def set_lbf(cls, force):
        return cls(force * 4.44822162)

    def get_lbf(self):
        return self.force / 4.44822162