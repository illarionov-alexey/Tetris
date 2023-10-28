n = int(input())
my_stack = ""
for _ in range(n):
    ch = input()
    my_stack += ch
for i in my_stack[::-1]:
    print(i)