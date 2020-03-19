'''
у матриці 4*4, що задана користувачем замініть всі від’ємні елементи на 0.
'''
import random
import numpy as np

# creating zero matrix according to user's input data
while True:
    try:
        n, m = int(input('Enter number of array rows: ')), \
               int(input('Enter number of array columns: '))
        break
    except ValueError:
        print('Enter an integer!')

a = np.zeros((n, m), dtype=int)

# elements input to "i" and "j" axis using double cycle to fill every element in created matrix


for i in range(n):
    for j in range(m):
        a[i, j] = random.randint(-10, 10)  # Sorry for using random, but I'm really bored of typing minus every time. I hope you'll understand me :)
print('Start matrix: ')
print(f'{a}')

# using double cycle to check the negative elements. All of them are reassigning to 0

for i in range(n):
    for j in range(m):
        if a[i, j] < 0:
            a[i, j] = 0
print('Final matrix: ')
print(f'{a}')
