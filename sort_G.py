n=int(input())
a=list(map(int, input().split()))
num, ind = map(int, input().split())
a.insert(ind-1,num)
print(" ".join(map(str,a)))