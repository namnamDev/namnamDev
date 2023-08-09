class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:

        arr = list(range(1, m+1))
        answer= []
        for now in queries:
            for i in range(m):
                if now == arr[i]:
                    arr = [arr[i]] + arr[:i] + arr[i+1:]
                    answer.append(i)
        return answer
