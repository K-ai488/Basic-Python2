count = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]   # 3次元配列の初期化　（１フロア１０部屋、３階建ての公舎４棟）
n = int(input())
k = 0
while n>k:
    b,f,r,v = map(int, input().split())
    count[b-1][f-1][r-1] += v  # 指定の部屋にv人を追加する
    k += 1
for i in range(4):
    if i !=0:
        print("####################")
    for j in range(3):
        for k in range(10):
            if k !=9:
                print("",count[i][j][k],end="")
            else:
                print("",count[i][j][k])
