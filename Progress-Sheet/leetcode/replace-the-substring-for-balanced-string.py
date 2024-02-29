class Solution:
    def balancedString(self, s: str) -> int:
        track = defaultdict(int)
        for cxr in s:
            track[cxr] += 1

        k = len(s) // 4
        surplus = defaultdict(int)
        for c in track: 
            if track[c] > k: 
                surplus[c] = track[c] - k
        
        if not surplus: 
            return 0
    
        extras = len(surplus)
        mini = len(s)
        left, right = 0 , 0

        while right < len(s):
            if s[right] in surplus: 
                surplus[s[right]] -= 1
                if surplus[s[right]] == 0: 
                    extras -= 1
            
            while extras == 0:
                mini = min(mini, right - left + 1)
                if s[left] in surplus:
                    surplus[s[left]] += 1
                    if surplus[s[left]] == 1: 
                        extras += 1 
                left += 1
            right += 1       
        
        return mini

        # optional approach
        # k = len(s)//4
        # ans = len(s)
        # right, left = 0, 0

        # while right < len(s):
        #     track[s[right]] -= 1

        #     while left < len(s) and all(track[i] <= k for i in track):
        #         ans = min(ans, right-left+1)
        #         track[s[left]] += 1
        #         left += 1
        #     right += 1  

        # return ans if ans != len(s) else 0

