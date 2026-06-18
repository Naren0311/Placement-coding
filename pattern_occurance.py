s=eval(input())
v='*'
freq={}
for i in s:
    freq[i]=freq.get(i,0)+1
for i in range(0,max(s)+1):
     if i in freq:
        print(f"{i}    {v * freq[i]}")
     else:
        print(f"{i}     ")
