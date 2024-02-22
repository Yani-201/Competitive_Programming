class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        track_end = defaultdict(int)
        for i in range(len(s)):
            track_end[s[i]] = i

        part_size = []
        cur_size, cur_end = 0, 0 
        
        for j in range(len(s)):
            cur_end = max(cur_end, track_end[s[j]])
            cur_size+=1
            if j == cur_end:
                part_size.append(cur_size)
                cur_size = 0

        return part_size
        