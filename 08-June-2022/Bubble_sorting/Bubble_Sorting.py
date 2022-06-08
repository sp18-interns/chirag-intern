# Bubble sort is a sorting algorithm that compares two adjacent elements and swaps them until they are not in the intended order.


def bubble_sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

nums = [3,6,12,1,35,0,2,6,4,36,68]
bubble_sort(nums)
print(nums)