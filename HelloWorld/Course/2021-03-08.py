h = 0
try:
    h = open('a.txt', 'r')
finally:
    print('finally', h)
    h.close()
