import functools

# 编写高阶函数，就是让函数的参数能够接收别的函数
def calc(a, b, func):
    return func(a) + func(b)


# map/reduce


# sort
def my_sort(L):
    return sorted(L, key=str.lower, reverse=True)


def by_name(t):
    return t[0]


# 闭包
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def lazy_sum(*args):
    def sum():
        s = 0
        for n in args:
            s += n
        return s
    return sum


# 内层函数能访问外层函数的变量，但不能修改它的指向
def createCounter():
    count = [0]

    def counter():
        count[0] += 1
        return count[0]

    return counter


# 而nonlocal关键字用来在函数或其他作用域中修改外层(非全局)变量
def create_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


# decorator
def logger(func):
    def wrapper(*args, **kw):
        print("before %s execute " % func.__name__)
        fn = func(*args, **kw)
        return fn
    return wrapper


def metrix(name=None):
    def decorate(func):
        def wrapper(*args, **kw):
            print("before %s execute " % func.__name__)
            fn = func(*args, **kw)
            if name is not None:
                print('%s has been logged' % name)
            return fn
        return wrapper
    return decorate


# 注解方法必须在之前被定义(书写顺序!!!)
@metrix()
def t():
    print('like this ?')


if __name__ == '__main__':
    print(calc(1, -1, abs))
    ls = ['bob', 'about', 'Zoo', 'Credit']
    print(my_sort(ls))
    li = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    # L = sorted(li, key=by_name())  # fixme
    c = [1, 2, 3, 4]
    print(lazy_sum(*c)())

    counterA = create_counter()
    print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
    counterB = createCounter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')

    L = list(filter(lambda x: x % 2 == 0, range(1, 20)))
    print(L)

    t()
    max2 = functools.partial(max, 55)
    print(max2(1, 55, 666))
    int2 = functools.partial(int, base=2)
    print(int2('100', base=10))