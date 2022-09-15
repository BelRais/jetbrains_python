# put your python code here
a = int(input())
q = 0
for i in range(a):
    w = a%10
    a = a//10
    q = q + w
print(q)
