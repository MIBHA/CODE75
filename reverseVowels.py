class Solution1:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU") #we can do this {'a','e','i','o','u','A','E','I','O','U'}
        con_list = list(s)         #converting string to list
        left, right = 0, len(s) - 1 #two pointers algo usage  

        while left < right:
            while left < right and con_list[left] not in vowels:  #moving left p to right until we find a vowel
                left += 1
            while left < right and con_list[right] not in vowels: #moving right p to left until we find a vowel
                right -= 1

            if left < right:
                con_list[left], con_list[right] = con_list[right], con_list[left]  #swapping
                left += 1
                right -= 1

        return ''.join(con_list)
s= Solution1()
print(f"'IceCreAm' -> '{s.reverseVowels('IceCreAm')}'")
print(f"'leetcode' -> '{s.reverseVowels('leetcode')}'")
print(f"'hello' -> '{s.reverseVowels('hello')}'")  # Test change
