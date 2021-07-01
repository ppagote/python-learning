def compare_input(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b


print(compare_input(7, 4))


def two_word(str):
    my_list = str.lower().split()
    if (my_list[0][0] == my_list[1][0]):
        return True


print(two_word('Prnav pago'))


def sum_integer(a, b):
    if a+b == 20 or a == 20 or b == 20:
        return True
    else:
        return False


print(sum_integer(10, 10))


def cappitalize(my_str):
    out_str = ''
    for key, value in enumerate(my_str):
        if key == 3 or key == 0:
            out_str += value.upper()
        else:
            out_str += value
    return out_str


print(cappitalize('pran'))


def reverse(my_str):
    my_list = my_str.split()
    my_list.reverse()
    return ' '.join(my_list)


print(reverse('pranav pajh'))


def check_inp(a):
    if 90 >= a <= 110 or 190 >= a <= 120:
        return True
    else:
        return False


print(check_inp(900))


def has_33(my_list):
    for y, x in enumerate(my_list):
        if x == 3:
            if my_list[y] == my_list[y+1]:
                return True
            else:
                return False


print(has_33([1, 3, 1, 3]))


def paper_doll(text):
    out = ''
    for x in text:
        out = out + x*3
    return out


print(paper_doll('Hello'))


def blackjack(a, b, c):
    out = a+b+c
    if out > 21 and (a == 11 or b == 11 or c == 11):
        out = out - 10
    if out <= 21:
        return out
    elif out > 21:
        return 'BUST'


print(blackjack(9, 9, 11))


def summer_69(arr):
    if(len(arr) != 0):
        out = 6 in arr and 9 in arr and arr.index(6) < arr.index(9)
        out_sum = 0
        print(arr.index(6))
        if(out):
            for x, y in enumerate(arr):
                print(x, y)
                if not x >= arr.index(6) and x <= arr.index(9):
                    out_sum += y
            return out_sum
    else:
        return 0


print(summer_69([]))


def spy_game(arr):
    final_str = ''
    for y in arr:
        if y == 0 or y == 7:
            final_str += str(y)

    if '007' in final_str:
        return True
    else:
        return False


print(spy_game([0, 0, 1, 4, 0, 7]))
