class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        arr1_freq=defaultdict(int)
        for j in range(len(arr1)):
            arr1_freq[arr1[j]]+=1
        
        sortt=[]
        for k in arr2:
            sortt.extend([k]*arr1_freq[k])
            del arr1_freq[k]

        not_in=[]
        for i in arr1_freq:
            not_in.extend([i]*arr1_freq[i])
        not_in.sort()
        sortt.extend(not_in)

        return sortt

        



        