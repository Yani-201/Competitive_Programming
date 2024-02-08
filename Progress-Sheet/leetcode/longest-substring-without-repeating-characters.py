class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track=set()
        length=0
        i,j=0,0
        while j<len(s):
            if s[j] in track:
                length=max(length, j-i)
                track.remove(s[i])
                i+=1
            else:
                track.add(s[j])
                j+=1

        length= max(length, j-i)
        return length
        