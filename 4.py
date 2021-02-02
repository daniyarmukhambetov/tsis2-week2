class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        res = 1
        nn = n
        a = []
        while nn > 0:
            a.append(nn%10)
            nn//=10
        for i in a:
            res*=i
        for i in a:
            res-=i
        # res=n-res
        return res