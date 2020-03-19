'''
виконайте добуток двох квадратних матриць 3*3, врахуйте розмірність.
Результати множення елементів занесіть до нової матриці та виведіть її на екран;
'''
col1, row2 = True, False

# entering the data about matriсes size

while col1 != row2:
    try:
        row1 = int(input('Number of your rows in 1st matrix: '))
        col1 = int(input('Number of your rows in 2nd matrix: '))
        row2 = int(input('Number of your columns in 1st matrix: '))
        col2 = int(input('Number of your columns in 2nd matrix: '))
    except ValueError:
        print("Enter an integer!")

# if entered data doesn't agree with matrix multiplication rules, the program will ask about new data

    if col1 != row2:
        print('Number of rows in 1st matrix does not equal to number of columns in 2nd matrix. Take account of this rule and try again.')
        input('Please, press "Enter" to continue ')
    else:
        print('Please, input 1st matrix: \n')               #filling the 1st matrix
        m1 = []
        for i in range(row1):                               #using the cycle to fill every element of 1st matrix to their list
            j = 0
            row = []
            while j != col1:
                row.append(float(input(f'Value of element of {i + 1} row, {j + 1} column: ')))
                j = j + 1
            m1.append(row)                                  # adding an every element to main list
            j = j + 1

                        #THERE WE ARE DOING ALL THE SAME OPERATIONS BUT FOR 2ND MATRIX

        print('Please, input 2nd matrix: \n')
        m2 = []
        for i in range (row2):
            j = 0
            row = []
            while j != col2:
                row.append(float(input(f'Value of element of {i + 1} row, {j + 1} column: ')))
                j = j + 1
            m2.append(row)
            i = i + 1

                        #THERE WE ARE MULTIPLYING TWO MATRICES AND FILL THE RESULT TO 3RD MATRIX

        m3 = []
        col2 = len(m2[0])
        a = -1                                          # a counter of rows
        for n in m1:                                    # recounting the rows of the first matrix
            new_row = []
            a = a + 1
            col_count = -1                              # a counter of columns
            while col_count != (col2 - 1):
                col_count += 1
                b = -1                                  # a counter of columns
                w = 0                                   # new matrix element
                for m in n:
                    b = b + 1
                    n_2 = m2[b]
                    m_2 = n_2[col_count]
                    new_m = m * m_2
                    w += new_m
                new_row.append(w)
            m3.append(new_row)                                  #filling the result to 3rd list named matrix number 3
        print('The result of multiplying your matrices: ', m3)
