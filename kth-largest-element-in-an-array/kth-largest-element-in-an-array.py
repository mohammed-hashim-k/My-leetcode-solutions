class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pos = self.partition(nums, 0, len(nums)-1)
        if pos > len(nums) - k:
            return self.findKthLargest(nums[:pos], k-(len(nums)-pos))
        elif pos < len(nums) - k:
            return self.findKthLargest(nums[pos+1:], k)
        else:
            return nums[pos]

        
    def partition(self, nums, l, r):
        index = random.randint(0, len(nums) - 1)
        nums[index], nums[r] = nums[r], nums[index]
        pivot = nums[r]
        lo = l 
        for i in range(l, r):
            if nums[i] < pivot:
                nums[i], nums[lo] = nums[lo], nums[i]
                lo += 1
        nums[lo], nums[r] = nums[r], nums[lo]
        return lo
        
        
        
        
        
        
        
        
    def naive(nums,k):
        ''' O(klogk)+O((n-k) log (n-k))'''
        import heapq
        res=[]
        for i in range(len(nums)):
            heapq.heappush(res,nums[i])
            if i>=k:
                heapq.heappop(res)
        return heapq.heappop(res)
        