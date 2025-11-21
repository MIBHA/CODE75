class Solution:
    def __init__(self, n: int):
        self.n = n

    def nNumbers(self, n: int):
        self.n = n
        print(f"The first {self.n} numbers are:")
        for i in range(1, self.n + 1):
            print(i, end=' ')

    def sumOfnNumbers(self):
        return (self.n*(self.n+1))//2
        print(f"The sum of first {self.n} numbers is: ")

s = Solution(100)
s.nNumbers()
s.sumOfnNumbers()