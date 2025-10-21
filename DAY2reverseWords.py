class day2:
    def reverseWords(self, s: str)-> str:   #we gonna return string
        words = s.split()                   #we split
        reversethewords= words[::-1]        #we reverse
        return " ".join(reversethewords)    #we join

s= day2()
print(s.reverseWords("Hello World"))
print(s.reverseWords("No melon No lemon"))