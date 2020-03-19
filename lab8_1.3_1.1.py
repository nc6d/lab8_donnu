'''
Виведіть на екран елементи лінійного масиву (заданий користувачем) у
зворотному порядку
'''
import numpy as np

while True:
    try:
        length = int(input('Enter power of array: '))
        break
    except ValueError:
        print('Enter the integer!')

# creating an zero array with needed size:

a = np.zeros(length, dtype=int)
arr_size = len(a)

# an simple elements input using cycle "for" to fill an zero array

for i in range(arr_size):
    a[i] = int(input("Input elements of your array: "))
print(f'Start array: {a}')

# reversing an array using the slice method

a2 = a[::-1]
print(f'Reversed array: {a2}')
