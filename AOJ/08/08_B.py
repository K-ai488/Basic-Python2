while True:
    n = int(input())
    if n==0:
        break
    i = 0                            #加算用
    while n!=0:
        i += n%10
        n = n//10
    print(i)
