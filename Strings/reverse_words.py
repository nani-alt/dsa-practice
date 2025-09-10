class Solution:
    def reverseWords(self, s):
       words=s.split(".")
       words=[w for w in words if w]
       words.reverse()
       
       return '.'.join(words)
