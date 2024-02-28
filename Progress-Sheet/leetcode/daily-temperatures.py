class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono = []
        ans = [0]*len(temperatures)

        for i in range(len(temperatures)): 
            while len(mono) > 0 and temperatures[i] > mono[-1][1]:
                now = mono.pop()
                ans[now[0]] = i - now[0]
            mono.append([i, temperatures[i]])
            
        return ans       