# ====================================================================================================
# Greedy Algorithm 1
# How much should I return change in order to save the number of coins maximum?
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
# Greedy Algorithm 2 
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
while n >= k:                                           # 1st while clause starts here  
    while n % k != 0:                                   # 2nd while clause whether n is not divisible to k
        n -= 1                                          # if so, we diminish 1 from n
        count += 1                                      # and count that action
    n //= k                                             # [IMPORTANT] if n is divisible to k, it doesn't enter the 2nd while clause, but divide n by k
    count += 1                                          # and count that action as well
# Substract 1 again
while n > 1:                                            # while n is superior to 1
    n -= 1                                              # we diminish 1 from n
    count += 1                                          # and it is also counted
print(count)                                            # final result

# Make any number to 1 by minimum number of attempt - 3rd attempt (Me)
n, k = map(int, input().split())
count = 0
while n >= k:
    if n % k != 0:
        n -= 1
        count += 1
    else:
        n //= k
        count += 1
while n > 1:
    n -= 1
    count += 1
print(count)
