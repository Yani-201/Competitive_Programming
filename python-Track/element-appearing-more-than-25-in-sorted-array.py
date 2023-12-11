class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        left, right = 0, floor(len(arr)*0.25)
        while right<len(arr):
            if arr[left] == arr[right]:
                return arr[left]
            else:
                left+=1
                right+=1
        # return 0

        