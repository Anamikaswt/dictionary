dic={'a':12,'b':8,'c':10,'d':6}
a=sorted(dic.values())
length=len(a)
i=length-1
list=[]
while i>=0:
    m=a[i]
    list.append(m)
    i=i-1
print(list)