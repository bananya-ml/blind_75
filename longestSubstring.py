'''
Given a string s, find the length of the longest 
substring without repeating characters.
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        '''
        :type s: str
        :rtype: int
        '''
        temp = set()
        l = 0
        res = 0
        for i in range(len(s)):
            while s[i] in temp:
                temp.remove(s[l])
                l += 1
            temp.add(s[i])
            res = max(res, i-l+1)

        return res


s = "dvdf"
print(Solution().lengthOfLongestSubstring(s))
