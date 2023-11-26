#program that prints numbers from 0 to 99
for i in range(100):
    separator = ',' if i < 99 else '\n'
    print('{:02}{}'.format(i, separator), end=" ")
