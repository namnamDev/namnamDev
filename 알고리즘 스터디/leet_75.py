class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count_arr = [0, 0, 0]

        for i in nums:
            count_arr[i] += 1

        total = sum(count_arr)
        idx = 0

        for i in range(total):

            while idx < 3 and not count_arr[idx]:
                idx += 1
            count_arr[idx] -= 1
            nums[i] = idx

