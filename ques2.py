T=int(input())
for j in range(0,T):
    cost= input().split()
    costg=int(cost[0])
    costp=int(cost[1])
    sum1=0
    sum2=0
    n=int(input())
    for i in range(0,n):
        q=input().split()
        q1=int(q[0])
        q2=int(q[1])
        sum1=sum1 + q1 * costg + q2 * costp
        sum2=sum2 + q1 * costp + q2 * costg

    print(min(sum1,sum2))
