'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
'''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lst = []
        for bracket in s:
            if bracket in ['(', '{', '[']:
                lst.append(bracket)
            else:
                if not lst:
                    return False
                else:
                    last = lst.pop()
                    if last != '(' and bracket == ')':
                        return False
                    if last != '{' and bracket == '}':
                        return False
                    if last != '[' and bracket == ']':
                        return False

        return not lst


s = "()"
print(Solution().isValid("()"))
