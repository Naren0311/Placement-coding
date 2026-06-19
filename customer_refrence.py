n=5
cus={}
n_c=int(input("Enter the number of customer:"))
for i in range(n_c):
    name =input("Enter the name of the customer")
    n_r=int(input("Enter the no. of references :"))
    l=[]
    for j in range(n_r):
        Ref_name=input("Enter the refer namke")
        l.append(Ref_name)
    cus[name]=l
purchase=2
refer=3
next_level=1
customer=input("Enter the customer Name :")
Amount=int(input("Enter the Amount :"))
res=[]
share=Amount/1000
for key,value in cus.items():
    if customer in value:
        res.append(customer)
        c=share*2
        res.append(c)
        org_key=key
        res.append(org_key)
        res.append(refer*share)
        for key1,value1 in cus.items():
            if org_key in value1:
                res.append(key1)
                res.append(share)
print(res)





