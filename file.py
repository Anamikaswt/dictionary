f=open("annu.txt","w")
f.write("anamika singh")
f.close()
s=open("annu.txt","r")
d=s.read()
print(d)
s.close()