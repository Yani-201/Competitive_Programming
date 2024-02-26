class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        # sortedd = []
        # mapp = dict(zip(heights, names))
        # heights.sort(reverse=True)
        # for height in heights:
        #     sortedd.append(mapp[height])
        # return sortedd

        # freq=defaultdict(int)
        # for i in range(len(heights)):

#...counting sort in reversed order
        
        offset=abs(min(heights))
        maxi=max(heights)+offset
        freq=[0]*(maxi+1)
        done=[]
        mapp={}
        for i in range(len(heights)):
            freq[heights[i]+offset]+=1
            mapp[heights[i]]=names[i]
        for j in range(len(freq)-1, -1, -1):
            if freq[j]!=0:
                done.extend([j-offset]*freq[j])
        for k in range(len(done)):
            names[k]=mapp[done[k]]
        return names
        

