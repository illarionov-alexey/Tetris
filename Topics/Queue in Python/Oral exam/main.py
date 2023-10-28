from collections import deque as deq
d = deq()
x = []
n = int(input())
for _ in range(n):
    cmd = input()
    lst = cmd.split(" ")
    if lst[0] == "READY":
        d.append(lst[1])
    elif lst[0] == "EXTRA":
        d.append(d.popleft())
    else:
        x.append(d.popleft())
for z in x:
    print(z)


