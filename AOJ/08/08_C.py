count = [0 for i in range(ord('z') - ord('a') + 1)]  #26個(a~zの個数カウント用)のリストを作成
while True:
    try:
        A = input().lower() #全て小文字として入力する
        for j in A:
            if ord('a') <= ord(j) <= ord('z'):
                count[ord(j)-ord('a')]+= 1
    except EOFError:
        break          #input を最後まで行う
for k in range(len(count)):
    print(chr(k+ord('a'))+ " : " +str(count[k]))
