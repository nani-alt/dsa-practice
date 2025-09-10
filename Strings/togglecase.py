class Solution:
    def toggleCase(self, s):
        # code here
        sen=""
        for ch in s:
            if ch>="A" and ch<="Z":
                i=ord(ch)+32
                sen+=chr(i)
            else:
                i=ord(ch)-32
                sen+=chr(i)
        return sen
        
