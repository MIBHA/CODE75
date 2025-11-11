import collections
import sys

class Day9:
    def __init__(self):
        self.char_stack= []
        self.char_queue= collections.deque()

    def pushCharacter(self, char):
        self.char_stack.append(char)

    def enqueueCharacter(self, char):
        self.char_queue.append(char)
    
    def popCharacter(self):
        return self.char_stack.pop()

    def dequeueCharacter(self):
        return self.char_queue.popleft()

s=input()

obj=Day9()   

l=len(s)

for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break

if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.") 
