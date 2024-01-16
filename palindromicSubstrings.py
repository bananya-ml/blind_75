'''
Given a string s, return the number of palindromic substrings in it.
'''


class Solution(object):
    def countSubstrings(self, s):
        '''
        :type s: str
        :rtype: int
        '''
        res = 0

        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res


s = "abc"
print(Solution().countSubstrings(s))
