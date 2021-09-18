"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
EQUAL = object()
SUBLIST = object()
SUPERLIST = object()
UNEQUAL = object()


def sublist(list_one, list_two):
    list_one = "\t".join([str(x) for x in list_one])
    list_two = "\t".join([str(x) for x in list_two])

    if list_one == list_two:
        return EQUAL

    elif list_one in list_two:
        return SUBLIST

    elif list_two in list_one:
        return SUPERLIST

    return UNEQUAL
