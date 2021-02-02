class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = int(0)
        n = int(0)
        n = int(len(nums))
        # for i in List:
        #     n+=1
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] == nums[j]:
                    ans+=1
        return ans