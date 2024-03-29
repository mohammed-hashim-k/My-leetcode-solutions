"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

'''O(N) time N= number of employees'''
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # hash map to store employeee id and corresponding emloyee
        
        employee_map= {e.id:e for e in employees}
        
        def dfs(id):
            employee = employee_map[id]
            
            return employee.importance+sum(dfs(e_id) for e_id in employee.subordinates )
        
        return dfs(id)
            