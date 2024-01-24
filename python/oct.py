s='hello,om'
l=s.split()
print(l)
l1=[]
s2=''
s3=''
i=0
while i<len(s):
    if i%2==0:
        s2=s2+s[i]
    else :
         s3=s3+s[i]

    i=i+1
print(s2)
print(s3)