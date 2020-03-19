# linear search algorithm

import numpy as np
import random
import timeit

flag = input("If you wanna randomize input data, press 'Enter'. To enter manually press any other key: ")

a = np.zeros(10, dtype=int)
x = int(input('Enter desired item: '))
n = len(a)

if flag == '':
    while True:
        try:
            d1, d2 = int(input('Enter the minimum random value: ')), \
                     int(input('Enter the maximum random value: '))
            for i in range(10):
                a[i] = random.randint(d1, d2)
            break
        except ValueError:
            print("Enter an integer!")
else:
    while True:
        try:
            for i in range(10):
                a[i] = int(input(f'Enter {i + 1} element: '))
            break
        except ValueError:
            print("Input an integer!")
print(a)

i = 0
count = 0
while i < n and a[i] != x:
    i += 1
    count += 2
if i == n:
    print('Element doesnt found')
else:
    print(f"Element {x} found at {i + 1} position")
print(f"Comparisons were executed {count} times")
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f"Program was executed by {t} seconds")
