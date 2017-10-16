def getMaxSubList(src_list, left, right):
    """
    寻找一个和最大的非空连续子列表
    分治法：
        将数组分为更小的两部分，分三种情况
        1）：最大非空数组在左边
        2）：最大非空数组右边
        3）：最大数组横跨中线
    :param src_list: 原列表
    :param 左索引
    :right 右索引
    :return: 最大子数组
    """

    if left == right:
        return left, right, src_list[left]

    mid = int((left + right) / 2)
    mid_left = mid
    mid_right = mid
    mid_result1 = float('-Inf')
    mid_result2 = float('-Inf')

    sum = 0
    i = mid
    # 如果最大连续数组跨越中间点，则自中间向左向右分别寻找最大数组
    # 当right - left = 1时，mid=left，所有下面两个循环没有考虑到right=mid的情况，所有下面的迭代中，左数组的循环的right = mid，右数组的left = mid+1
    while i >= left:
        sum += src_list[i]
        if sum > mid_result1:
            mid_result1 = sum
            mid_left = i
        i -= 1

    i = mid + 1
    sum = 0
    while i <= right:
        sum += src_list[i]
        if sum > mid_result2:
            mid_result2 = sum
            mid_right = i
        i += 1

    mid_result = mid_result1 + mid_result2

    # 在左数组中寻找
    left_left, left_right, left_result = getMaxSubList(src_list, left, mid)
    # 在右数组中寻找
    right_left, right_right, right_result = getMaxSubList(src_list, mid + 1, right)

    # 比较各种情况中的最大值
    if left_result >= mid_result and left_result >= right_result:
        return left_left, left_right, left_result
    elif mid_result >= right_result:
        return mid_left, mid_right, mid_result
    else:
        return right_left, right_right, right_result


if __name__ == '__main__':
    l = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

    (left, right, result) = getMaxSubList(l, 0, len(l) - 1)

    print(left, right, result)
    pass
