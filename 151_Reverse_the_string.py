class Solution(object):
    def reverseWords(self, s):
        a=s.split()
        a=a[::-1]    
        r=" ".join(a)
        return r