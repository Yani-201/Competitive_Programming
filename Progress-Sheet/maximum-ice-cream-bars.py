class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maxi=max(costs)
        counted=[0]*maxi

        for i in range(len(costs)):
            counted[costs[i]-1]+=1
        ctr=0
        for k in range(len(counted)):
            if counted[k]!=0:
                    n=coins//(k+1)
                    if counted[k]<=n:
                        coins-=((k+1)*(counted[k]))
                        ctr+=(counted[k])
                    else:
                        coins-=((k+1)*n)
                        ctr+=n

            if coins==0:
                break

        return ctr