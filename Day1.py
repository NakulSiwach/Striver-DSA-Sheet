# Day 1

class Solution:

    # 73. Set Matrix Zeroes
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        col = [-1 for q in range(n)]
        row = [-1 for q in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = 0
                    col[j] = 0

        for i in range(m):
            for j in range(n):
                if row[i] == 0 or col[j] == 0:
                    matrix[i][j] = 0
        return matrix

    # 118. Pascal's Triangle
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1,numRows):
            temp = [0 for i in range(i+1)]
            for j in range(len(temp)):
                if j == 0 or j == len(temp)-1:
                    temp[j] = 1
                else:
                    temp[j] = ans[i-1][j] + ans[i-1][j-1]
            ans.append(temp)
        return ans

    # 31. Next Permutation
    def nextPermutation(self, nums: List[int]) -> None:
        index = 0
        flag = 0
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                flag = 1
        if flag == 0:
            return nums.sort()
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break
        newindex = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[index]:
                newindex = i
                break
        nums[newindex], nums[index] = nums[index], nums[newindex]
        for i in range(index + 1, (len(nums) + index + 1) // 2):
            nums[i], nums[len(nums) + index - i] = nums[len(nums) + index - i], nums[i]
        return nums


    # 53. Maximum Subarray
    def maxSubArray(self, nums: List[int]) -> int:
        tempSum = 0
        maxSum = 0
        for i in range(len(nums)):
            tempSum += nums[i]
            if tempSum > maxSum:
                maxSum = tempSum
            if tempSum < 0:
                tempSum = 0
        if maxSum == 0:
            return max(nums)
        return maxSum

    # 75. Sort Colors
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        high = len(nums) - 1
        mid = 0
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums

    #121. Best Time to Buy and Sell Stock
    def maxProfit(self, prices: List[int]) -> int:
        minele = prices[0]
        tempsum = 0
        maxdiff = 0
        for i in range(1, len(prices)):
            if prices[i] < minele:
                minele = prices[i]
            tempsum = prices[i] - minele
            maxdiff = max(maxdiff, tempsum)
        return maxdiff