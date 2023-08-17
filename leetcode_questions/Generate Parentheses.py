class Solution(object):
    def generateParenthesis(self, n):

        result = []

        def generate(left, right, stack, part):
            if left == right == 0:
                result.append(part)
                return
            if left > 0:
                generate(left-1, right, stack+1, part+'(')
            if right > 0 and stack > 0:
                generate(left, right-1, stack-1, part+')')
        
        generate(n, n, 0, '')
        return result
        