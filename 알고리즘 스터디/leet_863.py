# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        dict_arr = {}
        def split_tree(node: TreeNode):
            if not dict_arr.get(node.val):
                dict_arr[node.val] = []
            if node.left != None:
                dict_arr[node.val].append(node.left.val)
                if not dict_arr.get(node.left.val):
                    dict_arr[node.left.val] = [node.val]
                split_tree(node.left)
            if node.right != None:
                dict_arr[node.val].append(node.right.val)
                if not dict_arr.get(node.right.val):
                    dict_arr[node.right.val] = [node.val]
                split_tree(node.right)
            return

        start = target.val
        split_tree(root)
        visit = {}
        for key in dict_arr:
            visit[key] = 0
        visit[start] = 1
        my_queue = deque([start])
        while my_queue:
            now = my_queue.popleft()
            now_line = dict_arr[now]
            if visit[now] <= k:
                for node in now_line:
                    if not visit[node]:
                        my_queue.append(node)
                        visit[node] = visit[now] + 1

        print(visit)
        answer = []
        for key in visit:
            if visit[key] == k+1:
                answer.append(key)
        return answer


