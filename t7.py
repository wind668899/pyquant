# def f(n):
#     if n==1 or n==2:
#         return 1
#     if n>2:
#         return f(n-1)+f(n-2)
#
#
#
# if __name__=='__main__':
#     a=int(input())
#     # b=list(map(int,input().split(' ')))
#     # print(a)
#     # print(b)
#     print(f(a))

#取有序数列中某节点为i（作为根节点）,这时把树分成了两部分左子树NUM( i - 1 )和右子树NUM( n-i ) , ( NUM( x ) 为不同左右子树的数量 )。
# 设二叉搜索树的个数为 F( i , n )，则 F( i , n ) = NUM( i - 1 ) * NUM( n - i ) 不同的二叉搜索树的总数 NUM( n )，
# 是对遍历所有 i( 1 ≤ i ≤ n ) 的 F( i , n ) 之和，所以NUM( n ) = 累加F( i , n ),可以推得：NUM( n ) = 累加 NUM( i - 1 ) * NUM( n - i );
# n=int(input())
# dp=[0]*(n+1)
# dp[0] = 1
# dp[1] = 1
# for i in range(2,n+1):
#     for j in range(1,i+1):
#         dp[i] += dp[j-1] * dp[i-j]
# print(dp[n])

n=int(input())
dp=[0]*10
dp[0]=1
dp[1]=1
for i in range(2,n+1):
    for j in range(0,i):
        dp[i]+=dp[i-j-1]*dp[j]
print(dp[n])