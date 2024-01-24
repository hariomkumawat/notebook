for _ in range(int(input())):
    store_freq = {}
    n = int(input())
    arr = list(map(int,input().split()))
    for num in arr:
        if num in store_freq:
            store_freq[num] += 1 
        else:
            store_freq[num] = 1 
    mx_freq = 0
    for num in store_freq:
        if store_freq[num] > mx_freq:
            mx_freq = store_freq[num]
    
    print(n - mx_freq)