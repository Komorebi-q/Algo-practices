# https://labuladong.online/zh/algo/data-structure-basic/shell-sort/

def sort(nums):
    n = len(nums)
    h = 1 
    
    while h < n / 3: 
        h = 3 * h + 1
    
    while h >= 1:
        sorted_index = h
        while sorted_index < n:
            i = sorted_index
            while i >= h:
                if nums[i] < nums[i - h]:
                    nums[i], nums[i - h] = nums[i - h], nums[i]
                else:
                    break
                i -= h
            sorted_index += 1
        h //= 3
    return nums

if __name__ == "__main__":
    nums = [3, 4, 1, 5, 9, 2, 6, 8, 7, 0]
    print(f"nums: {sort(nums)}")
