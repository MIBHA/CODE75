class AdvancedArithmetic(object):
    pass

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        sum= 0

        for i in range(1, n+1):
            if n % i == 0:
                sum += i 
        return sum



s= Calculator()
n= int(input())
print("I implemented: " + type(s).__bases__[0].__name__)
print(s.divisorSum(n))