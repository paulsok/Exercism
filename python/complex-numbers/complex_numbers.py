import math


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __radd__(self, other):
        if not isinstance(other, (int, float)):
            raise ValueError(f'unsupported type {type(other)}')
        return self + other

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
        return ComplexNumber(self.real + other, self.imaginary)

    def __rmul__(self, other):
        if not isinstance(other, (int, float)):
            raise ValueError(f'unsupported type {type(other)}')
        return ComplexNumber(other, 0) * self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)
        return ComplexNumber(self.real*other.real - self.imaginary * other.imaginary,
                             self.real*other.imaginary + self.imaginary * other.real)

    def __rsub__(self, other):
        if not isinstance(other, (int, float)):
            raise ValueError(f'unsupported type {type(other)}')
        return ComplexNumber(other, 0) - self

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
        return ComplexNumber(self.real - other, self.imaginary)

    def __rtruediv__(self, other):
        if not isinstance(other, (int, float)):
            raise ValueError(f'unsupported type {type(other)}')
        return ComplexNumber(other, 0) / self

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            other = ComplexNumber(other, 0)
        divider = other.real ** 2 + other.imaginary ** 2
        return ComplexNumber((self.real * other.real + self.imaginary * other.imaginary) / divider,
                             (self.imaginary * other.real - self.real * other.imaginary) / divider)

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        return ComplexNumber(math.cos(self.imaginary), math.sin(self.imaginary)) * math.exp(self.real)
