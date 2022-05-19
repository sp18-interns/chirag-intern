
def sum13(nums):
    a = 0
    if (len(nums) > 0):
        i = 0
        while i < len(nums):
            if (nums[i] != 13):
                a += nums[i]
                i += 1
            else:
                i += 2
                continue
        return a
    else:
        return 0
