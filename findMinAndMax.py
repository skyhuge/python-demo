def findMinAndMax(L):
    if len(L) == 0:
        return None, None
    if len(L) == 1:
        return L[0], L[0]
    for i in range(len(L)-1):
        now = L[i]
        next = L[i + 1]
        if i == 0:
            maxv = L[i + 1]
            minv = L[i]
        if now < next:
            if now <= minv:
                minv = now
            if next >= maxv:
                maxv = next
        else:
            if next <= minv:
                minv = next
            if now >= maxv:
                maxv = now
    tp = (minv, maxv)
    return tp


# 列表生成式
def to_lowercase(L):
    return [s.lower() for s in L if isinstance(s, str)]


# generator

# 意义：集合具有迭代意义
# 可迭代：iterable isinstance([], Iterable)
# 迭代器：iterator isinstance([], Iterator)
# 转化法：iterable 通过iter() 变成 iterator

if __name__ == '__main__':
    # ls = [1, 3, 5, 2, 6, 22, 4, 8, 6, 4, 10]
    ls = [1, 7]
    tp = findMinAndMax(ls)
    print(tp)
    li = ['Hello', 'World', 18, 'Apple', None]
    print(to_lowercase(li))
