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