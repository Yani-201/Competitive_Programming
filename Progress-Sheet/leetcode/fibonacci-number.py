class Solution:
    def fib(self, n: int) -> int:

        if n <= 1: return n
        return self.fib(n-1) + self.fib(n-2)

    # if we somehow store the already calculated fibonacci we can implement the code below which will greatly affect the time and space complexity
    # def __init__(self):
    #     self.visited ={0:0, 1:1}
    # def fib(self, n: int) -> int:
    #     if n in self.visited:
    #         return self.visited[n]
        
    #     first = self.fib(n-1)
    #     second = self.fib(n-2)
    #     self.visited[n] = first + second
    #     return first + second
        