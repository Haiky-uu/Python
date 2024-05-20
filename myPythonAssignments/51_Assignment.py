# 51 get a list a = [2,3,4,55,33,4,55,343,66,77,88,99] and write a program to
# find maximum sum of non-adjacent numbers


def findMaxSum(nums, N):

    def rec(idx, dp):
        if idx >= len(nums):
            return 0
        if dp[idx] != -1:
            return dp[idx]
        dp[idx] = max(rec(idx + 1, dp), nums[idx] + rec(idx + 2, dp))
        return dp[idx]

    return rec(0, dp)

def main():
    a = [5,5,10,100,10,5]
    n = len(a)
    print(findMaxSum(a,n))


if __name__ == '__main__':
    main()


