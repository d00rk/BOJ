#연속합
N = int(input())
dp = list(map(int, input().split()))
result = [dp[0]]
for i in range(N-1):
    result.append(max(result[i] + dp[i+1], dp[i+1]))

print(max(result))
