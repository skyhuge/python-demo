#! /usr/bin/env python3

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def my_append(self=None):
    if self is None:
        self = []
    self.append('end')
    return self

