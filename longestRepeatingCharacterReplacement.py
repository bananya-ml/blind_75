'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.
'''


class Solution(object):
    def characterReplacement(self, s, k):
        '''
        :type s: str
        :type k: int
        :rtype: int
        '''
        count = {}
        res = 0
        l = 0

        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)

            while (i - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, i-l+1)

        return res


s = "ABAB"
k = 2
print(Solution().characterReplacement(s, k))
