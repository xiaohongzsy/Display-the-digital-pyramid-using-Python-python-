n=10
for i in range(1,n+1):
    print(" "*(n-i),end="")#关键将空格键看作字符
    for j in range(1,i+1):
        print(j,end=" ")#从1，到1,2到1,2,3历遍
    if i>1:
        for k in range(i-1,0,-1):#从1,到2,1到3,2，1负一步数历遍
            print(k,end=" ")#不换行就变金字塔
    print()
    #看作
    # □□□1□□□
    #□12□1□
