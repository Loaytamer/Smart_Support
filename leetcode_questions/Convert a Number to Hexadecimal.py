class Solution(object):
    def toHex(self, num):
        if num == 0:
            return '0'

        if num < 0:
            num = 2**32 + num
    
        hex_digits = '0123456789abcdef'  # The hexadecimal digits
        result = ''  
        while num > 0:
            digit = num % 16  
            hex_digit = hex_digits[digit]  
            result = hex_digit + result  
            num //= 16  
    
        return result
