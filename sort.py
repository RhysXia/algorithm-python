class Sort:
    """
    排序算法
    """

    def __init__(self, src_list, compare_func):
        """
        初始化
        :param src_list: 待排列表
        :param compare_func: 比较函数，有两个参数a,b; return a>b
        """
        self.src_list = src_list
        self.compare_func = compare_func

    def insert_sort(self):
        """
        插入排序
        :return:返回排序后的列表
        """
        # 如果列表为空，则直接返回空列表
        if len(self.src_list) == 0:
            return self.src_list

        for i in range(1, len(self.src_list)):
            key = self.src_list[i]
            j = i
            while j > 0:
                if self.compare_func(key, self.src_list[j-1]):
                    break
                self.src_list[j] = self.src_list[j - 1]
                j -= 1
            self.src_list[j] = key
        return self.src_list





def func(a, b):
    return a > b


if __name__ == '__main__':
    l = [18, 19, 34, 65, 1, 3, 2, 5, 6]
    sortCls = Sort(l, func)
    for item in sortCls.insert_sort():
        print(item)
