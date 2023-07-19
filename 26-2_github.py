f = open('26-2.txt')
n = int(f.readline())

lst = []
for _ in range(n):
    time, type = f.readline().split()
    lst.append([int(time), type])

lst = sorted(lst)

count_M = 0
count_B = 0
count_B_prev = 0
count_M_prev = 0
last_B = 0
last_M = 0

for i in range(n):
    time, type = lst[i]
    if type == 'M':
        count_M += 1
        last_M = n - count_M + 1
        count_B_prev = count_B
    else:
        count_B += 1
        last_B = count_B
        count_M_prev = count_M
if count_M > count_B:
    print(last_M, count_B_prev)
else:
    print(last_B, count_M_prev)