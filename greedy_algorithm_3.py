# Greedy algorithm exercises

# 가장 최소/최대 횟수/합계를 구하는 문제들로 답을 구하려면, 어떤 환경이 되어야 하는지 먼저 생각할 것
# 거스름돈(가장 큰 단위 지폐/동전부터 지급), 1이 될 때까지(-1보다는 무조건 나누기), 큰 수의 법칙(무조건 제일 큰 수와 두 번째 큰 수)

# 설탕 배달
# 3kg 봉지, 5kg 봉지가 있음
# n kg 배달할 때, 최소 봉지로 배달하려면 어떻게 해야 할까?

# ATM
n = int(input()) # 5
t = list(map(int, input().split())) # 3 1 4 3 2
t.sort() # 1 2 3 3 4
s = 0
li = []
for i in t:
    s += i
    li.append(s)
result = 0
for j in li:
    result += j
print(result)    
    
# 최소 동전 갯수 (응용)
n, k = map(int, input().split()) # 10 4200
li = []
for i in range(n):
    money = int(input())
    li.append(money)
li.sort(reverse=True)
count = 0
for i in range(len(li)):
    count += (k//li[i])
    k %= li[i]
print(count)
  
# 거스름돈 (응용)
n = int(input()) # 380
rtrn_money = 1000-n # 620
yen=[500,100,50,10,5,1]
count = 0
for i in range(len(yen)):
    count += rtrn_money//yen[i]
    rtrn_money %= yen[i]
print(count)

# 보물 (최소값 계산하기)
# 1. 배열 a,b를 모두 재배치할 수 있다면:
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
answer = 0
for i in range(n):
    answer += a[i]*b[i]
print(answer)

# 2. a만 재배열 가능하고 b는 움직일 수 없다는 조건이 붙는다면:
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer = 0
for _ in range(n):
    answer += max(a)*min(b)
    a.remove(max(a))
    b.remove(min(b))
print(answer)
