class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis=[]
        for i in range(len(points)):
            d= ((points[i][0])**2) + ((points[i][1])**2)
            dis.append((d,points[i],))
        dis.sort()
        ans=[]
        for i in range(k):
            ans.append(dis[i][1])
        return ans
        