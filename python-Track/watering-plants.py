class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps=0
        current=capacity
        i=0
        while i<len(plants):
            if current>= plants[i]:
                steps+=1
                
                
            elif current<plants[i]:
                current=capacity
                steps+=(i*2)+1   

            current-=plants[i]
            i+=1
                
        return steps
        