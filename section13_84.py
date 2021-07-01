import random
import traceback

def gensquares(n):
    for num in range(n):
        yield num**2


print(list(gensquares(5)))

def rand_num(low,high,n):
    for num in range(n):
        yield random.randint(low, high)

print(list(rand_num(1, 10, 2)))

s= 'hellow'
print(list(iter(s)))

def test_excep():
    try:
        a = 1/0
    except Exception:
        traceback.print_exc()

print(test_excep())