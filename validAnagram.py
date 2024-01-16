'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''


class Solution(object):
    def isAnagram(self, s, t):
        '''
        :type s: str
        :type t: str
        :rtype: bool
        '''
        if len(s) != len(t):
            return False
        count = {}
        for c in s:
            count[c] = 1 + count.get(c, 0)
        for c in t:
            count[c] = -1 + count.get(c, 0)
        for v in count.values():
            if v != 0:
                return False
        return True


s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))
