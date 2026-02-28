def sort(nums):
    length = len(nums)
    min_index = 0
    sorted_index = 0
    while sorted_index < length:
        for i in range(sorted_index + 1, length):
            if nums[i] < nums[min_index]:
                min_index = i

        [nums[sorted_index], nums[min_index]] = [nums[min_index], nums[sorted_index]]

        sorted_index += 1
        min_index = sorted_index

    return nums


if __name__ == "__main__":
    nums = [3, 4, 1, 5, 9, 2, 1, 6]
    print(f"nums: {sort(nums)}")
