__author__ = 'ashin'


class Person:
    count = 0
    __slots__ = ()  # 父类如果没有声明slots,那么子类即使声明了也不起作用

    def __init__(self, name, age):
        self._name = name
        self._age = age
        Person.count += 1

    def self_print(self):
        print('name : %s , age : %s ' % (self._name, self._age))


class Std(Person):
    __slots__ = ('_name', '_age', '_score', 'weight')

    def __init__(self, name, age, score):
        super().__init__(name, age)
        self._name = name
        self._age = age
        self._score = score

    def print_score(self):
        print('name : %s , age : %s , score : %s' % (self._name, self._age, self._score))


class Animal:
    def __init__(self, type):
        self._type = type

    def self_print(self):
        print('type is %s ' % self._type)


def print_twice(obj):
    obj.self_print()


# isinstance 判断的时候不要用 or/and ,有坑
def is_instance(L):
    isinstance(L, (list, tuple))


if __name__ == '__main__':
    A = Person('M', 23)
    s = Std('ashin', 28, 100)
    t = s
    a = Animal('cat')

