class Solution:
    def swap(self, nums, index1, index2):

        while index2 > index1:
            nums[index1], nums[index2] = nums[index2], nums[index1]
            index1+=1
            index2-=1

    def pancakeSort(self, arr: List[int]) -> List[int]:
        last_index = len(arr)-1
        ans=[]

        while last_index > 0:
            cur_max = 0
            max_index = None
            for i in range(last_index+1):
                if cur_max < arr[i]:
                    cur_max = arr[i]
                    max_index = i

            self.swap(arr, 0, max_index)
            ans.append(max_index+1)
            self.swap(arr, 0, last_index)
            ans.append(last_index+1)

            last_index-=1

        return ans


        
        