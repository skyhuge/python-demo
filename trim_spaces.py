
def trim_space(string):
    strs = str(string)
    ret = strs
    if strs[0:1] == ' ' and strs[strs.__len__()-1:strs.__len__()] == " ":
        ret = strs[1:strs.__len__()-1]
    elif strs[0:1] == " ":
        ret = strs[1:strs.__len__()]
    elif strs[strs.__len__()-1:strs.__len__()] == ' ':
        ret = strs[0:strs.__len__()-1]
    print(ret)


def trim(string):
    str = ''
    for i in range(len(string)):
        if string[i:i] != ' ':
            pass  # todo


if __name__ == '__main__':
    # trim_space('   ')
    if trim_space('hello  ') != 'hello':
        print('测试失败!')
    elif trim_space('  hello') != 'hello':
        print('测试失败!')
    elif trim_space('  hello  ') != 'hello':
        print('测试失败!')
    elif trim_space('  hello  world  ') != 'hello  world':
        print('测试失败!')
    elif trim_space('') != '':
        print('测试失败!')
    elif trim_space('    ') != '':
        print('测试失败!')
    else:
        print('测试成功!')
