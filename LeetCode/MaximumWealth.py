class Solution:
    def maximumWealth(self, accounts):
        max_wealth = 0
        for i in range(len(accounts)):
            current_wealth = 0
            for j in range(len(accounts[i])):
                current_wealth += accounts[i][j]
            max_wealth = max(max_wealth, current_wealth)
        return max_wealth

sol = Solution()
print(sol.maximumWealth([[1,5,7], [16,2,1], [10,3,5]]))