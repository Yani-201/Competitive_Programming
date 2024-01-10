class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        s=set()
        chemistry=0
        i=0
        j=len(skill)-1
        while j>i:
            s.add(skill[i]+skill[j])
            chemistry+=(skill[i]*skill[j])
            i+=1
            j-=1
        if len(s)==1:
            return chemistry
        else:
            return -1