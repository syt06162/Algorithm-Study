def solution(n):
    dp = [-1 for i in range(0,n+1)]
    dp[0] = 1
    dp[2] = 3
    for i in range(4, n+1, 2):
        dp[i] = dp[i-2]*3
        j = i-4
        while j>=0:
            dp[i] += dp[j]*2 
            j -= 2
        
        dp[i] %= 1000000007
    
    return dp[n]