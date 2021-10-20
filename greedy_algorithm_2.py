# 3rd greedy algorithm - 큰 수의 법칙
# n, m, k: n개의 숫자가 주어지고 그 가운데 m횟수만큼 더하되, 한 숫자를 k번 이상 연속 더하면 안됨
# n=5, m=8, k=3, li=[2,4,5,4,6] --> 6+6+6+5+6+6+6+5 = 46
import time
import sys
n, m, k = map(int, sys.stdin.readline().rstrip().split()) # NOTE: input() almost equals to sys.stdin.readline().rstrip() and the last one is way faster than the previous one
li = list(map(int, sys.stdin.readline().rstrip().split()))
start = time.time()
li.sort()
first = li[-1]
second = li[-2]
answer = 0
while True:
    for i in range(k):            # repetition for the biggest number in the list li
        if m == 0:
            break
        else:
            answer += first
            m -= 1
    if m == 0:                    # after adding the biggest number k times, we need to add the second biggest one (in order not to surpass 4 times the same number)
        break
    else:
        answer += second
        m -= 1
print(answer) 
end = time.time()
print(f"Second(s): {end-start}")
