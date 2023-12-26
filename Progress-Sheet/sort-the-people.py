class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        sortedd = []
        mapp = dict(zip(heights, names))
        heights.sort(reverse=True)
        for height in heights:
            sortedd.append(mapp[height])
        return sortedd

#...Bubble Sort in reverse order
        # for i in range(len(heights)):
        #     swaps=0
        #     for j in range(len(heights)-i-1):  
        #         if heights[j]<heights[j+1]:
        #             heights[j], heights[j+1] = heights[j+1], heights[j]
        #             swaps+=1 
        #             names[j], names[j+1] = names[j+1], names[j]
        #     if swaps==0:
        #         break 


#...Selection sort but in reversed order
        # for i in range(len(heights)):
        #     maxi=i
        #     for j in range(i+1, len(heights)):
        #         if heights[j]>heights[maxi]:
        #             maxi=j
        #     heights[i], heights[maxi] = heights[maxi], heights[i]
        #     names[i], names[maxi] = names[maxi], names[i]

#...Insertion sort but reverse
        # for i in range(len(heights)):
        #     pivot=heights[i]
        #     for j in range(i+1, len(heights)):
        #         if heights[j]>pivot:

        #         elif heights[j]<pivot:


        # return names