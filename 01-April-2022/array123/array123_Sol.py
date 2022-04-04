def array123(nums):
    for x in range(len(nums)-2):
        if nums[x] == 1 and nums[x+1] == 2 and nums[x+2] == 3:
            return True
    return False
    # num1=len(nums)

    # ls = list(nums)
    # if ls in nums[0:num1]:
    # return True
