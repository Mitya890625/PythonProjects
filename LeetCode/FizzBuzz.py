class Solution:
    def FizzBuzz(self, n):
        answer = []
        for i in range(1, n+1):
            answer.append(i)
        for i in range(0, n):
            if answer[i] % 3 == 0 and answer[i] % 5 == 0:
                answer[i] = 'FizzBuzz'
                continue
            if answer[i] % 3 == 0:
                answer[i] = 'Fizz'
                continue
            if answer[i] % 5 == 0:
                answer[i] = 'Buzz'
                continue
            else:
                answer[i] = str(i+1)
        return answer


sol = Solution()
print(sol.FizzBuzz(150))
