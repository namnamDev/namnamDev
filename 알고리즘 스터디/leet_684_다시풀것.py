#아무리 생각해도 훌륭한 코드가 생각이 안나서 답지 참조

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)

        adj = defaultdict(list)

        def cycleExists(curr, prev):
            if curr in visited: # cycle exists
                return True
            
            visited.add(curr) # visited this node
 
            for adjNode in adj[curr]: # checking out 
                if adjNode != prev and cycleExists(adjNode, curr):
                    return True
        
        for f, t in edges:
            visited = set()
            # adding this edge
            adj[f].append(t)
            adj[t].append(f)

            # checking if cycle exists 
            if cycleExists(f, t):
                return [f, t]
