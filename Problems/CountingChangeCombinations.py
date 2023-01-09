def count_change(money, coins):
    dp = [1]+[0]*money
    for coin in coins:
        for x in range(coin,money+1):
            dp[x] += dp[x-coin]
    return dp[money]


print(count_change(10, [5,2,3]))