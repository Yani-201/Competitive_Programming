class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def checkwin(start, end, turn):
            if start == end:
                return nums[start]
            if start > end:
                return 0

            if turn:
                turn = False
                startScore = checkwin(start+1, end, turn)
                endScore = checkwin(start, end-1, turn)
                return max(startScore + nums[start], endScore+nums[end]) 
    
            else:
                turn = True
                startScore = checkwin(start+1, end, turn)
                endScore = checkwin(start, end-1, turn)
                return min(startScore - nums[start], endScore-nums[end])


        return checkwin(0, len(nums)-1, True) >= 0
        