class Solution(object):
    def addBinary(self, a, b):
        i, j = len(a) - 1, len(b) - 1
        c = 0
        res = []
        def add_bits(bit_a, bit_b, carry):
            s = bit_a + bit_b + carry
            if s == 3:
                return '1', 1
            elif s == 2:
                return '0', 1
            elif s == 1:
                return '1', 0
            else:
                return '0', 0
        while i >= 0 or j >= 0 or c > 0:
            if i >= 0:
                val_a = int(a[i])
            if i < 0:
                val_a = 0
            if j >= 0:
                val_b = int(b[j])
            if j < 0:
                val_b = 0
            out_bit, c = add_bits(val_a, val_b, c)
            res.append(out_bit)
            i -= 1
            j -= 1
        return "".join(reversed(res))


