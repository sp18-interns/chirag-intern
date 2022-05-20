def sum67(nums):
    record = True
    total = 0
    for n in nums:
        if n == 6:
            record = False
        if record:
            total += n
            continue
        if n == 7:
            record = True
    return total

    # for i in range(len(nums)):
    #   for j in range(len(nums)):
    #     if i == 6 and j == 7:
    #       return nums.pop(nums[i]:nums[j])
    # return sum(nums)
