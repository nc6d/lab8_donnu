# binary search algorithm

import numpy as np
import random
import timeit

flag = input("If you wanna randomize input data, press 'Enter'. To enter manually press any other key: ")

a = np.zeros(10, dtype=int)

n = len(a)

if flag == '':
    while True:
        try:
            d1, d2 = int(input('Enter the minimum random value: ')), \
                     int(input('Enter the maximum random value: '))
            x = int(input('Enter desired item: '))
            break
        except ValueError:
            print("Enter an integer!")

    for i in range(10):
        a[i] = random.randint(d1, d2)
else:
    while True:
        try:
            x = int(input('Enter desired item: '))
            for i in range(10):
                a[i] = int(input(f'Enter {i + 1} element: '))
            break
        except ValueError:
            print("Enter an integer!")

a = sorted(a)
print(a)
l = 0
r = len(a) - 1
k = 0
count = 0

flag = False
while l <= r and not flag:
    count += 2
    k = (l + r) // 2
    if a[k] == x:
        flag = True
    elif a[k] < x:
        count += 1
        l = k + 1
    else:
        count += 1
        r = k - 1
if not flag:
    print('Element is not found')
else:
    print(f'Element {x} is found at {k + 1} position')
print(f"Comparisons were executed {count} times")
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f"Program was executed by {t} seconds")
