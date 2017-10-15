import sort


def func(a, b):
    return a > b


if __name__ == '__main__':
    l = [18, 19, 34, 65, 1, 3, 2, 5, 6]
    sortCls = sort.Sort(l, func)
    for item in sortCls.insert_sort():
        print(item)
