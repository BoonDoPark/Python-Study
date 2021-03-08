# try:
#     4 / 0
# except ZeroDivisionError as e:
#     print(e)
#
# print('aaaa')

# try:
#     f = open('a.txt', 'r')

f = None
try:
    f = open('a.txt', 'r')
    # f = open('b.txt', 'r')
except FileNotFoundError as e:
    print(e)
finally:
    print('finally', f)
    if f:
        while True:
            line = f.readline()
            if not line:
                break
            print(line)

        print('im closed')
        f.close()
