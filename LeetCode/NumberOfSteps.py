class Solution:
    def NumberOfSteps(self, num):
        counter = 0 
        while num != 0:
            if num % 2 == 0:
                num /= 2
            elif num % 2 != 0:
                num -= 1
            counter += 1
        return counter
sol = Solution()
print(sol.NumberOfSteps(1))