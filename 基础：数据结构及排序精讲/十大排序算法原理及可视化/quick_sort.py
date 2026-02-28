# https://labuladong.online/zh/algo/data-structure-basic/quick-sort/

def sort(nums, lo, hi):
    def partition(nums, lo, hi):
        pivot = nums[lo]
        i = lo + 1
        j = hi
        while i <= j:
            while i < hi and nums[i] <= pivot: 
                i += 1
            while j > lo and nums[j] > pivot:
                j -= 1
            if i >= j:
                break
            [nums[i], nums[j]] = [nums[j], nums[i]]
        nums[lo], nums[j] = nums[j], nums[lo]

        return j
    
    if lo >= hi:
        return
    p = partition(nums, lo, hi)
    sort(nums, lo, p - 1)
    sort(nums, p + 1, hi)
    
    return nums
    
    

if __name__ == "__main__":
    nums = [3, 4, 1, 5, 9, 2, 6, 8, 7, 0]
    print(f"nums: {sort(nums, 0, len(nums) - 1)}")
            
                
            
            