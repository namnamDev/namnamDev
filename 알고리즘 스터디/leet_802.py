class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        result = [0] * n

        def dfs(node: int) -> bool:
            if result[node] != 0: return result[node] == 2
            result[node] = 1
            for neighbor in graph[node]:
                if result[neighbor] == 1 or not dfs(neighbor): return False
            result[node] = 2
            return True

        safe_nodes = []
        for node in range(n):
            if dfs(node): safe_nodes.append(node)

        return safe_nodes
