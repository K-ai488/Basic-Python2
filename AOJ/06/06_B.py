cards = [[0 for i in range(13)] for j in range(4)]
pattern = ["S","H","C","D"]          #S➡️0,H➡️1,C➡️2,D➡️3としたい
n = int(input())
k = 0
while n>k:
    a, r = input().split()
    r = int(r) 
    cards[pattern.index(a)][r-1] = 1  # rは0からなのでズレる
    k += 1
for i in range(0,4):
    for j in range(0,13):
        if cards[i][j] == 0:
            print(pattern[i],j+1)
