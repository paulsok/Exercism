def equilateral(sides):
    return len(set(sides)) == 1 and min(sides) > 0


def isosceles(sides):
    sides = sorted(sides)

    return len(set(sides)) <= 2 and sides[0] + sides[1] > sides[2]


def scalene(sides):
    sides = sorted(sides)

    return len(set(sides)) == 3 and sides[0] + sides[1] > sides[2]
