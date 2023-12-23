class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered=defaultdict(int)
        for i in range(len(ranges)):
            for j in range(ranges[i][0], ranges[i][1]+1):
                covered[j]+=1

        for k in range(left, right+1):
            if k not in covered:
                return False
        return True