# def merge(nums, lo, mid, hi):
#     temp = nums[0 : len(nums)]
#     i = lo
#     j = mid + 1

#     for p in range(lo, hi + 1):
#         if i == mid + 1:
#             nums[p] = temp[j]
#             j += 1
#         elif j == hi + 1:
#             nums[p] = temp[i]
#             i += 1
#         elif temp[i] > temp[j]:
#             nums[p] = temp[j]
#             j += 1
#         else:
#             nums[p] = temp[i]
#             i += 1


# def sort(nums, lo, hi):
#     if lo == hi:
#         return
#     mid = lo + (hi - lo) // 2
#     sort(nums, lo, mid)
#     sort(nums, mid + 1, hi)
#     merge(nums, lo, mid, hi)

#     return nums


def merge(nums, lo, mid, hi):
    temp = nums[lo : hi + 1]
    i = lo
    j = mid + 1

    for p in range(lo, hi + 1):
        if i == mid + 1:
            nums[p] = temp[j - lo]
            j += 1
        elif j == hi + 1:
            nums[p] = temp[i - lo]
            i += 1
        elif temp[i - lo] > temp[j - lo]:
            nums[p] = temp[j - lo]
            j += 1
        else:
            nums[p] = temp[i - lo]
            i += 1


def sort(nums, lo, hi):
    # 单个元素不用排序
    if lo == hi:
        return
    mid = lo + (hi - lo) // 2
    sort(nums, lo, mid)
    sort(nums, mid + 1, hi)
    merge(nums, lo, mid, hi)

    return nums


if __name__ == "__main__":
    nums = [3, 4, 1, 5, 9, 2, 6, 8, 7, 0]
    print(f"nums: {sort(nums, 0, len(nums) - 1)}")
