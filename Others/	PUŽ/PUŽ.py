a,b,v=map(int,input().split())
x=(v-a+(a-b))/(a-b)
if x==int(x):
    print(int(x))
else:
    print(int(x)+1)
