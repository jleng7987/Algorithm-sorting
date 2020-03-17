n=int(input())
k=int(input())
w = list(map(int, input().split()))
v = list(map(int, input().split()))

def beibao(n, k, w, v):
    dp = [[0 for j in range(k + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= w[i - 1] and dp[i][j] < dp[i - 1][j - w[i - 1]] + v[i - 1]:
                dp[i][j] = dp[i - 1][j - w[i - 1]] + v[i - 1]
    # for x in dp:
    #     print(x)
    return dp[-1][-1]

print(beibao(n,k,w,v))