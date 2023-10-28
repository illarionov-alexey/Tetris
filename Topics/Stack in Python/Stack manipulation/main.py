import collections as cols
#n = input()
d = cols.deque()
d.pop()
for _ in range(int(n)):
    cmd = input()
    lst = cmd.split(" ")
    if lst[0] == "PUSH":
        d.append(lst[1])
    else:
        d.pop()
while len(d)>0:
    print(d.pop())

