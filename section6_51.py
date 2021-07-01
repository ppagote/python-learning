import string


def ran_check(num, low, high):
    if low <= high and num >= low and num <= high:
        return True
    else:
        return False


print(ran_check(4, 3, 4))


def up_low(s):
    upper_count = 0
    lower_count = 0
    for x in s:
        if x.isupper():
            upper_count += 1
        elif x.islower():
            lower_count += 1
    return {"No. of Upper case characters": upper_count, "No. of Lower case Characters": lower_count}


print(up_low('PrAnav A'))


def unique_list(lst):
    return list(set(lst))


print(unique_list([1, 1, 1, 3, 2, 4, 5, 5, 6]))


def multiply(numbers):
    out = 1.0
    for num in numbers:
        out *= num
    return out


print(multiply([1, 3, -4]))


def palindrome(s):
    s = s.replace(' ', '')
    if s == s[::-1]:
        return True
    else:
        return False


print(palindrome('dada'))


def ispangram(str1):
    a = []
    b = string.ascii_lowercase
    for x in str1.lower():
        if x in b:
            a.append(x)
    print(len(set(a)))
    if len(set(a)) == len(b):
        return True
    else:
        return False


def ispangram1(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset.issubset(set(str1.lower()))


print(ispangram1('The quick brown fox jumps over the lazy dog!!!'))
