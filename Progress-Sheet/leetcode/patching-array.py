class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        avail = deque(nums)
        patch = []

        cur = avail.popleft()
        summ = 0

        while summ < n:
            new = summ + 1
            if cur and new >= cur:
                summ += cur
                if avail:
                    cur = avail.popleft()
                else:
                    cur = None
            else:
                patch.append(new)
                summ += new
            print(new)

        return len(patch)
        