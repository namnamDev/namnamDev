class Solution:
    def numTeams(self, rating: List[int]) -> int:
        size = len(rating)
        to_right_larger_list = [0] * size
        to_right_smaller_list = [0] * size
        to_left_larger_list = [0] * size
        to_left_smaller_list = [0] * size

        for f in range(size):
            for s in range(f + 1, size):
                if rating[f] > rating[s]:
                    to_right_smaller_list[f] += 1
                    to_left_larger_list[s] += 1
                else:
                    to_right_larger_list[f] += 1
                    to_left_smaller_list[s] += 1

        answer = 0
        for idx in range(1, size - 1):
            answer += to_right_larger_list[idx] * to_left_smaller_list[idx]
            answer += to_left_larger_list[idx] * to_right_smaller_list[idx]

        return answer
