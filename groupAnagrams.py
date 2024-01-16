from collections import Counter
'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''


class Solution(object):
    def groupAnagrams(self, strs):
        '''
        :type strs: List[str]
        :rtype: List[List[str]]
        '''
        anagrams = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]

        return list(anagrams.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))
