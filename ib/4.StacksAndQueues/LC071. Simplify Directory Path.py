'''
Given an absolute path for a file (Unix-style), simplify it.

Examples:

path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
Note that absolute path always begin with ‘/’ ( root directory )
Path will not have whitespace characters.
'''
class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for d in path.split('/'):
            if d == '..' and stack:
                stack.pop()
            elif d == '' or d == '.':
                pass
            else:
                stack.append(d)
        return '/' + '/'.join(stack)

# test
print('/a/./b/../../c/'.split('/'))
print(Solution().simplifyPath('/a/./b/../../c/'))
