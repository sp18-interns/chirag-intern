# # def same_first_last(nums):
# #     if nums[0] == nums[-1] and len(nums) >= 1:
# #         return True
# #     else:
# #         return False


# # if __name__ == '__main__':
# #     same_first_last([1, 2, 1])


# def string_match(a, b):
#     count = 0
#     for i in range(len(a)-1):
#         for j in range(len(b)-1):
#             if a[i:i+2] == b[j:j+2]:
#                 print(f"{a[i:i+2]} and {b[j:j+2]}")
#                 count += 1
#     return count


# print("Abu")

# print(string_match('aabbccdd', 'abbbxxd'))


# def string_match1(a, b):
#     # Figure which string is shorter.
#     shorter = min(len(a), len(b))
#     count = 0

#     # Loop i over every substring starting spot.
#     # Use length-1 here, so can use char str[i+1] in the loop
#     for i in range(shorter-1):
#         a_sub = a[i:i+2]
#         b_sub = b[i:i+2]
#         if a_sub == b_sub:
#             print(f"{a_sub} and {b_sub}")
#             count = count + 1

#     return count


# print(string_match1('aabbccdd', 'abbbxxd'))

# def string_match(a, b):
#     count = 0
#     print(range(len(a)-1) and range(len(b)-1))
#     for i in range(len(a)-1) and range(len(b)-1):
#         # for j in range(len(b)-1):
#         if a[i:i+2] == b[i:i+2]:
#             #print(f"{a[i:i+2]} and {b[j:j+2]}")
#             count += 1
#     return count


# print(string_match('aabbccdd', 'abbb'))


def make_pi():
    pi = 22/7.0
    pi = str(pi)
    pi = list[pi]
    pi = pi[:1]+pi[2:4]
    pi = [int(x) for x in pi]
    return pi
