class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        # Idhi gpt ichindhi na badhamakam valla type cheyaley nenu 3 loops thos run chesina but 2 loops inka optimal basic ga  e idea 0ms latency speeed tho execute chesina valla code lo chusina
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        prefix_max = nums[0]

        if prefix_max - suffix_min[0] <= k:
            return 0

        for i in range(1, n):
            prefix_max = max(prefix_max, nums[i])

            if prefix_max - suffix_min[i] <= k:
                return i

        return -1