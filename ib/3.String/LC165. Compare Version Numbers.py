'''
Compare two version numbers version1 and version2.

If version1 > version2 return 1,
If version1 < version2 return -1,
otherwise return 0.
You may assume that the version strings are non-empty and contain only digits
and the . character.
The . character does not represent a decimal point and is used to separate
number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is
the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 1.13 < 1.13.4
'''
class Solution:
    # make two version numbers the same length and then comapre
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = [int(i) for i in version1.split('.')]
        version2 = [int(i) for i in version2.split('.')]
        m, n = len(version1), len(version2)
        if m < n:
            version1.extend([0] * (n - m))
        else:
            version2.extend([0] * (m - n))
        for v1, v2 in zip(version1, version2):
            if v1 > v2:
                return 1
            if v1 < v2:
                return -1
        return 0

    # compare common part and compare sum of remaining
    def compareVersion2(self, version1, version2):
        version1 = [int(i) for i in version1.split('.')]
        version2 = [int(i) for i in version2.split('.')]
        min_len = min(len(version1), len(version2))
        # comapre common part
        for i in range(min_len):
            if version1[i] > version2[i]:
                return 1
            if version1[i] < version2[i]:
                return -1
        # compare remaining. eg: 1.1 vs 1.1.0.0.0
        # use slicing to avoid checking which version is longer
        if sum(version1[min_len:]) > sum(version2[min_len:]):
            return 1
        elif sum(version1[min_len:]) < sum(version2[min_len:]):
            return -1
        else:
            return 0

# test
print(Solution().compareVersion('0.1', '1.1'))
print(Solution().compareVersion('1.1', '1.2'))
print(Solution().compareVersion('1.2', '1.13'))
print(Solution().compareVersion('1.13', '1.13.4'))
print(Solution().compareVersion2('0.1', '1.1'))
print(Solution().compareVersion2('1.1', '1.2'))
print(Solution().compareVersion2('1.2', '1.13'))
print(Solution().compareVersion2('1.13', '1.13.4'))
