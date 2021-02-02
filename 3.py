class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur = 0
        ans = 0
        for i in gain:
            cur += i
            if cur > ans:
                ans = cur
        return ans
        