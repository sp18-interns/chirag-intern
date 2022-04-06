def rotate_left3(nums):
    # nums[0] = nums[len(nums-1)]
    # return nums
    # n = len(nums)
    # return nums[1:(n-1)] + nums[0]
    return [nums[1], nums[2], nums[0]]
