# coding:utf-8
class Sort:
    """
    排序算法
    """

    def __init__(self, src_list: list, compare_func):
        """
        初始化
        :param src_list: 待排列表
        :param compare_func: 比较函数，有两个参数a,b; return a>b
        """
        self.src_list = src_list.copy()
        self.compare_func = compare_func
        # 执行次数
        self.count = 0

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
                self.count += 1
                if self.compare_func(key, self.src_list[j - 1]):
                    break
                self.src_list[j] = self.src_list[j - 1]
                j -= 1
            self.src_list[j] = key
        return self.src_list

    def heap_sort(self):
        """
        堆排序
        :return:
        """
        length = len(self.src_list)
        while length > 0:
            self.__update_all_heap__(length)
            temp = self.src_list[length - 1]
            self.src_list[length - 1] = self.src_list[0]
            self.src_list[0] = temp
            length -= 1
        return self.src_list

    def __update_all_heap__(self, length: int):
        """
        对列表进行堆排序
        :return:
        """
        index = int((length - 1) / 2)
        while index >= 0:
            self.__update_one_heap__(index, length)
            index -= 1
        pass

    def __update_one_heap__(self, index: int, length):
        """
        更新堆，使索引所在的子树成为最大堆
        :param index:
        :return:
        """
        self.count += 1
        largest_index = index
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        # 有左子结点
        if left_index < length and self.compare_func(self.src_list[left_index], self.src_list[largest_index]):
            largest_index = left_index
        # 有右子结点
        if right_index < length and self.compare_func(self.src_list[right_index], self.src_list[largest_index]):
            largest_index = right_index
        if largest_index != index:
            # 交换
            temp = self.src_list[index]
            self.src_list[index] = self.src_list[largest_index]
            self.src_list[largest_index] = temp
            # 更新子树
            self.__update_one_heap__(largest_index, length)

    def quick_sort(self):
        """
        快速排序
        :return:
        """
        self.__quick_sort__(0, len(self.src_list) - 1)
        return self.src_list
        pass

    def __quick_sort__(self, left, right):
        if left < right:
            mid = self.__partition__(left, right)
            self.__quick_sort__(left, mid - 1)
            self.__quick_sort__(mid + 1, right)
        pass

    def __partition__(self, left: int, right: int):
        """
        对数组给定范围内进行重拍，将[right]排到正确位置并且返回索引
        :param left:
        :param right:
        :return:
        """
        item = self.src_list[right]
        i = left
        p = i
        while i < right:
            if not self.compare_func(self.src_list[i], item):
                self.__swap(i, p)
                p += 1
            i += 1
            self.count += 1
        self.__swap(right, p)
        return p
        pass

    def __swap(self, index1: int, index2: int):
        """
        交换
        :param index1: 索引1
        :param index2: 索引2
        :return:
        """
        temp = self.src_list[index1]
        self.src_list[index1] = self.src_list[index2]
        self.src_list[index2] = temp
        pass


def func(a, b):
    return a > b


import matplotlib.pyplot as plt
import random

if __name__ == '__main__':
    L1 = []
    i = 0
    X = []
    Y1 = []
    Y2 = []
    Y3 = []
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    while i < 150:
        X.append(len(L1))
        L1.append(random.randint(1, 100))
        sortClass1 = Sort(L1, func)
        # L2 = sortClass.heap_sort()
        sortClass1.insert_sort()
        Y1.append(sortClass1.count)
        sortClass2 = Sort(L1, func)
        sortClass2.heap_sort()
        Y2.append(sortClass2.count)
        sortClass3 = Sort(L1, func)
        r = sortClass3.quick_sort()
        Y3.append(sortClass3.count)
        i += 1
    plt.title(u'排序算法效率对比')
    plt.xlabel(u"数组长度")
    plt.ylabel(u"计算次数")
    p1 = plt.plot(X, Y1, label='insert sort')
    p2 = plt.plot(X, Y2, label='heap sort')
    p3 = plt.plot(X, Y3, label='quick sort')
    plt.legend(loc='upper left')
    plt.show()
    # l = [51, 12, 2, 15, 84, 188, 16, 41, 48]
    # sortCls = Sort(l, func)
    # result = sortCls.quick_sort()
    # print(result)
