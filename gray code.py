from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        l=[]
        l.append(0)
        if n==0:
            return l
        l.append(1)
        curr=1
        for i in range(2,n+1):
            curr=curr*2
            for j in range(n-1,-1,-1):
                l.append(curr+l[j])

        return l

s=Solution()
print(s.grayCode(0))