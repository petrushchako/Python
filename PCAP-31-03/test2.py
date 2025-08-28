from math import floor
import py_compile  # Allows to compile modules where they may be optimized to not evaluate assertions

assert 1 == 1.0, "The integer 1 should equal the float 1.0"


def round_down(num):
    return floor(num)


assert 6 == round_down(6.999), " round_down should always round a float down"

try:
    assert -5 == round_down(-5.999), " round_down should always round a float down"
except AssertionError as exception:
    print("Handle AssertionError 1:", exception)


try:
    if __debug__:
        if -5 != round_down(-5.999):
            raise AssertionError(" round_down should always round a float down")
except AssertionError as exception:
    print("Handle AssertionError 2:", exception)

print("Assertion are evalued if __debug__ is True")
print("The value of the __debug__ is : ", __debug__)
print("Modules executed normally have __debug__ set to True")
print('Modules executed with "python -O" have __debug__ set to False')
