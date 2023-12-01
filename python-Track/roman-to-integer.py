class Solution:
    def romanToInt(self, s: str) -> int:
        mapping={"I":1, "V": 5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        sum=0
        i=0
        while i < len(s):
            if s[i:i+2] in ("IV", "IX", "XL", "XC", "CD", "CM"):
                sum+=(mapping[s[i+1]] - mapping[s[i]])
                i+=2
                continue
            sum+=mapping[s[i]]
            i+=1
        return sum
            