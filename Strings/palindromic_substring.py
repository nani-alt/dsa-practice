class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        n=len(s)
        for i in range(n):
            for j in range(i+1,n+1):
                if s[i:j]==s[i:j][::-1]:
                    count+=1
        return count
