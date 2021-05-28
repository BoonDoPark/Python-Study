class Converter:
    def convert_to_dec(self, bin: str):
        decimal = int(bin, 2)
        print(decimal)

    def convert_to_bin(self, dec):
        binary = bin(dec)
        print(binary)
        # 0b1010
        # 0 binary 1010
        # 1010
        # -> 1*2^3 + 0*2^2 + 1*2*1 + 0*2*0
        # = 8 + 2 = 10

    def convert_to_oct(self, dec):
        octet = oct(dec)
        print(octet)
        # 0o12
        # 0 octet 12
        # 12
        # -> 1*8^1 + 2*8^0
        # = 8 + 2 = 10

    def convert_to_hex(self, dec):
        hexa = hex(dec)
        print(hexa)
        # 0xa
        # 0 hexa a
        # a
        # -> a(10)16^0
        # = 10*1 = 10


class BitOperator:
    def bit_and(self, bit1: int, bit2: int):
        res = bin(bit1 & bit2)
        print(res)

    def bit_or(self, bit1: int, bit2: int):
        res = bin(bit1 | bit2)
        print(res)

    def bit_xor(self, bit1: int, bit2: int):
        res = bin(bit1 ^ bit2)
        print(res)

    def bit_not(self, bit: int):
        # 1의 보수
        res = bin(~bit)
        print(res)

    def left_shift(self, bit: int, i: int):
        tmp = bit << i
        res = bin(tmp)
        print('decimal : ', tmp)
        print(res)

    def right_shift(self, bit: int, i: int):
        tmp = bit >> i
        res = bin(tmp)
        print('decimal : ', tmp)
        print(res)


dec = 10
converter = Converter()
converter.convert_to_bin(dec)
converter.convert_to_oct(dec)
converter.convert_to_hex(dec)
converter.convert_to_dec('1010')
print(type(0b1010))  # int

op = BitOperator()
b1 = 0b11110000
b2 = 0b10101010
op.bit_and(b1, b2)
op.bit_or(b1, b2)
op.bit_xor(b1, b2)
op.bit_not(b1)

print('\n', int(str(b1)))
op.left_shift(b1, 2)  # 240 -> 480 -> 960
op.right_shift(b1, 2)  # 240 -> 120 -> 60


print('\n', int(str(b2)))
op.left_shift(b2, 3)
op.right_shift(b2, 3)
