class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        track = defaultdict(lambda: -1)
        mono_stack = []

        for i in range(len(nums2)):

            while len(mono_stack)>0 and mono_stack[-1] < nums2[i]:
                new = mono_stack.pop()
                track[new] = nums2[i]
            mono_stack.append(nums2[i])

        ans = []
        for j in range(len(nums1)):
            ans.append(track[nums1[j]])

        return ans



        