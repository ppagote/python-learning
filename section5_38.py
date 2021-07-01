st = 'Print only the words that start with s in this sentence'
for char in st.split():
    if (char.lower().startswith('s')):
        print(char)

for x in range(0, 11, 2):
    print(x)

print(list(range(0, 11, 2)))

my_list = [num for num in range(1, 50) if num % 3 == 0]
print(my_list)

st = 'Print every word in this sentence that has an even number of letters'
for char in st.split():
    if (len(char) % 2) == 0:
        print(char)

for num in range(1, 101):
    if num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    elif num % 5 == 0 and num % 3 == 0:
        print('FlizzBuzz')
    else:
        print(num)

st = 'Create a list of the first letters of every word in this string'
my_list2 = [alpha[0] for alpha in st.split()]
print(my_list2)
