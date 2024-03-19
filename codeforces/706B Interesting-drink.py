def count_shops(n, prices, q, coins):
    prices.sort()
    result = []
    
    for i in range(q):
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if prices[mid] <= coins[i]:
                low = mid + 1
            else:
                high = mid - 1
        result.append(low)
    
    return result

n = int(input())
prices = list(map(int, input().split()))
q = int(input())
coins = [int(input()) for _ in range(q)]

result = count_shops(n, prices, q, coins)

for res in result:
    print(res)
