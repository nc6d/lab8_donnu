'''
виведіть на екран транспоновану матрицю 3*3 (початкова матриця задана
користувачем).
'''
import numpy as np

while True:
    try:
        row_num, col_num = int(input('Enter number of array rows: ')), \
                           int(input('Enter number of array columns: '))
        break
    except ValueError:
        print('Enter the integer!')

# Creating an zero matrix with needed size according to length and width:

a = np.zeros((row_num, col_num), dtype=int)

# Elements input to "i" and "j" axis using double cycle to fill every element in created matrix

for i in range(row_num):
    for j in range(col_num):
        a[i, j] = int(input(f'Enter {i, j} element: '))
print(f'{a} (Main matrix)')

# Matrix transposition.
# We are using an lists generator to create a new matrix with list elements instead of tuples:

b = ([list(x) for x in zip(*a)])
print(f'{b} (Transparent matrix) ')
