loop=int(input('Total number of loops:'))
l=[5,4,2,1]
start_r=l[loop%4]
total_r=2*loop
res=[]
R=[]
for num1 in range(0,loop):
    num2=loop%4 +num1
    if num2>3:
        num2=num2%4
    res.append(l[num2])
res=res[::-1]
for num3 in range(0,int((total_r)/2)):
    if num3==0:
        R_s=1+2*res[num3]
        R_p=R_s/(1+R_s)
        R.append(R_s)
        R.append(R_p)
    elif num3==int(((total_r)/2)-1):
        R_s=R_p+1+2*res[num3]
        R.append(R_s)
    else:
        R_s=R_p + 2*res[num3]
        R_p=R_s/(1+R_s)
        R.append(R_s)
        R.append(R_p)
R=R[::-1]
I=1/R[0]
curr=[]
curr.append(I)
res=res[::-1]
for num4 in range(0,loop):
    if num4==0:
        i=1-I*(1+2*res[num4])
        it=I-i
    elif num4==(loop-1):
        i=it
    else:
        i=i-2*res[num4]*it
        it=it-i
    curr.append(i)
print('Current from battery:',curr[0])
print('Current in each branch:',curr[1:])
q=str(input('Press enter to exit'))
