'''
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
'''


class Solution(object):
    def encode(sefl, strs):
        '''
        @param: strs: a list of strings
        @return: encoded string
        '''
        res = ""
        for s in strs:
            res += str(len(s)) + '&' + s
        return res

    def decode(self, str):
        '''
        @param: str: a string
        @return: decoded list of strings
        '''
        res = []
        i = 0
        while i < len(str):
            j = i
            while str[j] != '&':
                j += 1
            length = int(str[i:j])
            res.append(str[j+1: j + 1 + length])
            i = j + 1 + length
        return res


strs = ["lint", "4code", "love", "you"]
s = Solution().encode(strs)
print(Solution().decode(s))
