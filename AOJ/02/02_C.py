a,b,c = map(int, input().split())
l = [a,b,c]
l = sorted(l)
l=[str(i) for i in l]
l=" ".join(l)         #リストの内容だけを取り出す操作
print(l)
