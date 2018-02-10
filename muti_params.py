def calc(nums):
    sum = 0
    for n in nums:
        sum += n
    return sum


# 可变参数
def add_nums(*nums):
    sum = 0
    for n in nums:
        sum += n
    return sum


# 关键字参数
def print_nums(name, age, **kw):
    #  kw.clear()  # 对kw的操作不会改变extra的值
    print('name is %s , age is %s , other is %s' % (name, age, kw))


# 命名关键字参数
def print_info(name, age, *args, addr, job):
    print('name is %s , age is %s , addr is %s , job is %s ' % (name, age, addr, job))
    print('* is ', args)  # args 其实是一个只有一个元素的tuple


# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def example(a, b=1, *, c, d, **kw):
    print(a, b, c, d, kw)


def exam(*args, **kw):
    print(args.__add__((6,)), kw)


if __name__ == '__main__':
    l = [1, 2, 4, 3, 5]
    print(calc(l))
    print(add_nums(*l))
    extra = {'job': 'Engineer', 'address': 'Shanghai'}
    print_nums('ashin', 24, gender='male')
    print_nums('ashin', 24, **extra)
    print_info('ashin', 24, extra, addr='China', job='Engineer')
    example('hello', c='adc', d='world', **extra)
    exam(*l, **extra)
