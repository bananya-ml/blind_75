'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
'''


class Solution(object):
    def minWindow(self, s, t):
        '''
        :type s: str
        :type t: str
        :rtype: str
        '''
        if t == "":
            return ""
        countT, map = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        h, n = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0

        for i in range(len(s)):
            c = s[i]
            map[c] = 1 + map.get(c, 0)

            if c in countT and map[c] == countT[c]:
                h += 1
            while h == n:
                if (i - l + 1) < resLen:
                    res = [l, i]
                    resLen = (i - l + 1)
                map[s[l]] -= 1
                if s[l] in countT and map[s[l]] < countT[s[l]]:
                    h -= 1
                l += 1

        l, i = res
        return s[l:i+1] if resLen != float("inf") else ""


s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow(s, t))
