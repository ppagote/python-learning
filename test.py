my_num = [1, 2, 3, 4, 5, 6]


def check_even(num):
    return num % 2 == 0


print(list(map(check_even, my_num)))
print(list(filter
           (check_even, my_num)))

my_num[0] = 2
m_list = [0, 1, [0, 1, [0, 1]]]
print(m_list)

l = [0, 1, 0]
