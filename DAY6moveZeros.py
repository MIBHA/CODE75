class Day6:
    def moveZeroes(self, nums: list[int]) -> None:
        w_ptr= 0
        for r_ptr in range(len(nums)):
            if nums[r_ptr] != 0:  
                nums[w_ptr] = nums[r_ptr]   
                w_ptr += 1

        for i in range(w_ptr, len(nums)):
            nums[i] = 0

s= Day6()
num_list2 = [0,1,0,3,12]
s.moveZeroes(num_list2)
