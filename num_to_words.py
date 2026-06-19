num=int(input("Enter the number :" ))
num_1word = ['one', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'nine', 'Zero']
num_2word = ['Ten', 'Twenty', 'Thirty', 'Fourty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninty']
numbers_dict = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

temp=int(num)
t=int(num)
t1=int(num)
count=0
lis=[]
while temp>0:
    d=temp%10
    lis.append(d)
    count+=1
    temp//=10



if count==1:
    print(num_1word[num-1])
if count==2:
    x= t % 10
    y=x
    x1=t//10
    print(x1)
    if x==0:
        print(num_2word[x1-1])
    elif t1>10 and t1<20:
        print(numbers_dict[t-11])
    else:
        print(f"{num_2word[x1-1]}{num_1word[y-1]}")
   
       
if count==3:
    if lis[0]==0 and lis[1]==0:
        print(f"{num_1word[lis[2]-1]} hundered")
    elif lis[1]==0:
         print(f"{num_1word[lis[2]-1]} hundered {num_1word[lis[0]-1]}")
    else:
        print(f"{num_1word[lis[2]-1]} Hundered {num_2word[lis[1]-1]} {num_1word[lis[0]-1]} ")



        
    
    
   
