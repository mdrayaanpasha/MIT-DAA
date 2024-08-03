def LT(coins):
    n = len(coins)
    
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i]=coins[i]
        
        
    for k in range(2,n+1):
        for i in range(n-k+1):
            j= i + k - 1
            
            pick_i = coins[i] + min(
                dp[i+1][j-1] if i+1 <= j-1 else 0,
                dp[i+2][j] if i+2 <= j else 0
                )
            pick_j = coins[j] + min(
                dp[i][j-2] if j-2 >= i else 0,
                dp[i+1][j-1] if j-1 >= i+1 else 0
                )
            
            dp[i][j] = max(pick_i,pick_j);
            
    
    return dp[0][n-1]
        
        
coins = [3, 9, 1, 2]
print(LT(coins))
