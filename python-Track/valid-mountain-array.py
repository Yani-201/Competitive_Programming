class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        inc= False
        dec= False

        for i in range(len(arr)-1):
            if arr[i]<arr[i+1] and not dec:
                inc=True
            elif arr[i]>arr[i+1] and inc:
                dec=True
            else: 
                return False
                
        if inc and dec:
            return True
        else:
            return False


        