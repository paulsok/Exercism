from __future__ import division
from math import gcd


class Rational:
    def __init__(self, numer, denom):
        g = gcd(numer, denom)
        if denom < 0:
            denom = -denom
            numer = -numer

        self.numer = numer//g
        self.denom = denom//g


    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = (self.numer*other.denom) + (other.numer*self.denom)
        denom = (self.denom*other.denom)
        return Rational(numer, denom)

    def __sub__(self, other):
        denom = (self.denom*other.denom)
        numer = (self.numer*other.denom) - (other.numer*self.denom)
        return Rational (numer, denom)

    def __mul__(self, other):
        result = Rational(self.numer * other.numer, self.denom * other.denom)
        return result

    def __truediv__(self, other):
        result = Rational(self.numer * other.denom, self.denom * other.numer)
        return result

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        return Rational(self.numer**power, self.denom**power)

    def __rpow__(self, base):
        return base**(self.numer/self.denom)
        