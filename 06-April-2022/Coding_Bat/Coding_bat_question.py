# Logic-2 > make_bricks


'''We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks


make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True'''


def make_bricks(small, big, goal):
    if (small + big*5) < goal:
        return False
    elif small < goal % 5:
        return False
    else:
        return True


# Logic-2 > lone_sum
'''Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.


lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0'''


def lone_sum(a, b, c):
    if a == b and b == c and a == c:
        return 0
    elif a == b:
        return c
    elif b == c:
        return a
    elif a == c:
        return b
    elif a != b != c:
        return a+b+c


#  lucky_sum
'''Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.


lucky_sum(1, 2, 3) → 6
lucky_sum(1, 2, 13) → 3
lucky_sum(1, 13, 3) → 1'''


def lucky_sum(a, b, c):

    if a == 13:
        return 0
    if b == 13:
        return a
    if c == 13:
        return a+b
    else:
        return a+b+c


#  no_teen_sum
'''Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().


no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3
no_teen_sum(2, 1, 14) → 3'''


def no_teen_sum(a, b, c):
    teen = [13, 14, 17, 18, 19]
    if a in teen and b in teen and c in teen:
        return 0
    elif a in teen and b in teen and c not in teen:
        return c
    elif a in teen and c in teen and b not in teen:
        return b
    elif b in teen and c in teen and a not in teen:
        return a
    elif a in teen and b not in teen and c not in teen:
        return b + c
    elif c in teen and a not in teen and b not in teen:
        return a + b
    elif b in teen and a not in teen and c not in teen:
        return a + c
    return a + b + c


# round_sum
'''For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().


round_sum(16, 17, 18) → 60
round_sum(12, 13, 14) → 30
round_sum(6, 4, 4) → 10'''


def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)


def round10(n):
    num_str = repr(n)
    last_digit_str = num_str[-1]
    if 1 <= last_digit_str < 5:
        return 0


# double_char
'''Given a string, return a string where for every char in the original, there are two chars.


double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree''''


def double_char(str):
    str2 = ""
    for i in str:
        str2 = str2+i+i
    return str2


# count_hi
'''Return the number of times that the string "hi" appears anywhere in the given string.


count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2'''


def count_hi(str):
    return str.count('hi')


# cat_dog
'''
Return True if the string "cat" and "dog" appear the same number of times in the given string.


cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True'''


def cat_dog(str):
    count_cat = 0
    count_dog = 0
    for i in range(len(str)):
        x = str[i:i+3]
        if x == "cat":
            count_cat += 1
        if x == "dog":
            count_dog += 1
    return (count_cat == count_dog)


# count_code


'''Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.


count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2'''


def count_code(str):
    count = 0
    for i in range(len(str)-3):
        cur = str[i:i+4]
        if cur[0:2] == "co" and cur[3] == "e":
            count += 1
    return count


# end_other
'''Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.


end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True'''


def end_other(a, b):
    a1 = a.lower()
    b1 = b.lower()
    if a1.endswith(b1) or b1.endswith(a1):
        return True
    else:
        return False


# xyz_there
'''Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.


xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True'''


def xyz_there(str):
    for i in range(len(str)):
        x1 = str[i:i+4]
        y1 = str[i+1:i+4]
        z1 = str[i:i+3]
        #print(x1, y1, z1)
        if (i == 0 and z1 == "xyz") or (x1 != ".xyz" and y1 == "xyz"):
            return True
    return False
