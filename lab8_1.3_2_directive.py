# directive search of substring algorithm
import random
import timeit

text = "Hello World! I love Python!"
flag = input("If you wanna randomize input data, press 'Enter'. To enter manually press any other key: ")

if flag == '':
    str_find = ['Python', 'World', 'love']
    pattern = random.choice(str_find)
    print(f'Desired string is "{pattern}"')

else:
    pattern = input('Enter string to desire: ')
    print(f'Desired string is "{pattern}"')
i = -1
j = 0
count = 0
while (j < len(pattern)) and i < (len(text) - len(pattern)):
    j = 0
    i += 1
    count += 2
    while j < len(pattern) and pattern[j] == text[i + j]:
         j += 1
         count += 2
if j == len(pattern):
    print(f'Substring is found in {i + 1} position')
else:
    print('Substring is not found')
t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(f"Program was executed by {t} seconds")
