class day3:
    def compress(self, chars: list[str])-> int:
        r_ptr = 0  # read pointer
        w_ptr = 0  # write pointer

        while r_ptr < len(chars):
            current_char = chars[r_ptr]
            count = 0

            while r_ptr < len(chars) and chars[r_ptr] == current_char:
                r_ptr += 1
                count += 1

            chars[w_ptr] = current_char
            w_ptr += 1

            if count > 1:
                for digit in str(count):
                    chars[w_ptr] = digit
                    w_ptr += 1
        return w_ptr
    
s= day3()
char_list1 = ["a","a","b","b","c","c","c"]
lenght1 = s.compress(char_list1)
print(lenght1)  
print(char_list1[:lenght1])