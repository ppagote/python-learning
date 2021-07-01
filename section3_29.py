print(4 * (6 + 5))
print(4 * 6 + 5)
print(4 + 6 * 5)
type(3 + 1.5 + 4)
print(4**1/2)
print(2**2)
print('hello'[1])
print('hello'[::-1])
print('hello'[-1])
print('hello'[4:])

list3 = [1, 2, [3, 4, 'hello']]
list3[2][2] = 'goodbye'
print(list3)

list4 = [5, 3, 4, 6, 1]
list4.sort()
print(list4)

d = {'simple_key': 'hello'}
print(d['simple_key'])

d = {'k1': {'k2': 'hello'}}
print(d['k1']['k2'])

d = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

d = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

list5 = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]
print(set(list5))
print(3.0 == 3)
