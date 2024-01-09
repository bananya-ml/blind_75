'''
Reverse bits of a given 32 bits unsigned integer.
'''


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(format(n, 'b').zfill(32)[::-1], 2)


n = 0b0000010100101000001111010011100
print(Solution().reverseBits(n))
