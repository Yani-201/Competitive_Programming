class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)
        times=0
        for i in range(3,len(tasks),4):
            idx=i//4
            times=max(times,tasks[i]+processorTime[idx])
        # print(times)
        return times

        