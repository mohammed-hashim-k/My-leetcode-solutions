class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        '''pop the smallest grid each time and update the time 
           that is the maximum of least nodes we are considering
           each time '''
        N=len(grid)
        pq=[(grid[0][0],0,0)]
        seen=set([0,0])
        res=0
        
        while True:
            T,x,y= heapq.heappop(pq)
            res=max(res,T)
            
            if x==y==N-1:
                return res
            
            for i,j in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
                if 0<=i <N and 0<=j<N and (i,j) not in seen:
                    seen.add((i,j))
                    heapq.heappush(pq,(grid[i][j],i,j))