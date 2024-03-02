class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = defaultdict(int)
        for cxr in t:
            count_t[cxr] += 1

        window = defaultdict(int)
        l, r = 0, 0
        min_len = float('inf')
        left = 0

        for right in range(len(s)):
            window[s[right]] += 1

            while left <= right and all(window[c] >= count_t[c] for c in count_t):
                if window[s[left]] > 0:
                    window[s[left]] -= 1
                old_min = min_len
                min_len = min(min_len, right-left+1)
                if old_min > min_len:
                    r = right
                    l = left
                left += 1
        
        return s[l:r+1] if min_len != float('inf') else ''