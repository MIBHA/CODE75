class day5:
    def increaingTripletSubsequence(self, nums: list[int]) -> bool:
        f_num = s_num = float('inf')
        for n in nums:
            if n <= f_num:
                f_num = n
            elif n <= s_num:
                s_num = n
            else:
                return True
        return False
s= day5()
num_list1 = [1,2,3,4,5]
print(s.increaingTripletSubsequence(num_list1))