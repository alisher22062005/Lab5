camel_string=input()
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result=""
cnt=0
for i in camel_string:
    for j in alphabet:
        if i==j:
            result=result+"_"+i.lower()
            cnt+=1
    if cnt==0:
        result=result+i
    else:
        cnt=0
print(result)