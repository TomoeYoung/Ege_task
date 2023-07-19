f = open('26-1.txt')
n, m, k = map(int, f.readline().split())

hall = [[] for _ in range(m)]
lst = []

for _ in range(n):
    time, row, price = map(int, f.readline().split())
    lst.append([time, row, price])
lst = sorted(lst, key=lambda x: (x[0], -x[2]))

s_all = 0
last_row = 0

for i in range(n):
    time, row, price = lst[i]
    if len(hall[row - 1]) < k:
        hall[row - 1].append(price)
        last_row = row
        s_all += price

print(s_all, last_row)