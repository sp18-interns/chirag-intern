# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
name = set([])
for i in range(n):
    name.add(input())
print(len(name))
