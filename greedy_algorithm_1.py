# Greedy Algorithm 1 - how much should I return change in order to save the number of coins maximum?
def greedy(money): # 9380
    coin = [500, 100, 50, 10]
    count = 0
    for i in range(len(coin)):
        count += (money // coin[i])
        money %= coin[i]
    return count

print(greedy(9380))
# 25
        
# it shows how many coins have been used
def greedy2(money):
    coin = [500, 100, 50, 10]
    count = 0
    for i in range(len(coin)):
        count += (money // coin[i])
        print(f"Coin {coin[i]}: {money // coin[i]}")
        money %= coin[i]
    return f"Total: {count}"

print(greedy2(9830))
# Coin 500: 19
# Coin 100: 3
# Coin 50: 0
# Coin 10: 3
# Total: 25

# ====================================================================================================

# Make any number to 1 by minimum number of attempt - 1st attempt
n, k = map(int, input().split()) # n must be bigger than k
count = 0
while True:
    if n == 1:
        break
    if n % k == 0:
        n /= k 
        count += 1
    else: 
        n -= 1
        count += 1
print(count)
    
# Make any number to 1 by minimum number of attempt - 2nd attempt (Book)
n, k = map(int, input().split())
count = 0
# Unlimited division of n by k under the condition of n >= k 
while n >= k:
    while n % k != 0:
        n -= 1
        count += 1
    n //= k
    count += 1
# Substract 1 again
while n > 1:
    n -= 1
    count += 1
print(count)
