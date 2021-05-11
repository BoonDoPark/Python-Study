singer = {
    'name': 'BTS',
    'member': 7,
    '데뷔곡': '데인저',
    '대표곡': ['IDOL', '봄날', '불타오르네', 'Dynamite']

}

print(singer.values())

b = list(singer.values())
print(b)

for i in range(0, len(b), 1):
    print(b[i])
c = b[len(b) - 1]
for i2 in range(0, len(c), 1):
    print(c[i2])
