class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        graph = defaultdict(list)
        for i in range(1, n):
            graph[parent[i]].append(i)
        
        new_parent = parent.copy()
        
        for node in range(1, n):
            curr = parent[node]
            while curr != -1:
                if s[curr] == s[node]:
                    new_parent[node] = curr
                    break
                curr = parent[curr]
        
        new_graph = defaultdict(list)
        for i in range(1, n):
            new_graph[new_parent[i]].append(i)
        
        def dfs(node: int) -> int:
            size = 1
            for child in new_graph[node]:
                size += dfs(child)
            return size
        
        answer = []
        for i in range(n):
            answer.append(dfs(i))
            
        return answer
