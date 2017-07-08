row=int(input('Number of rows:'))
col=int(input('Number of columns:'))
mat=[]
b=[]
X=[0]*col
for num1 in range(0,row):
    a=[]
    for num2 in range(0,col):
        print('for matrix A element',(num1+1),(num2+1))
        ele=float(input('Enter element value'))
        a.append(ele)
    mat.append(a)
for num3 in range(0,row):
    print('for matrix b element',(num3+1),'1')
    bb=float(input('Enter element value'))
    b.append(bb)
from romil import t_mat_mul,check,replacement,interchange,sol_check,back_sub,trp,mat_mul,matrix_m
if row==col:
    ch=check(mat,row,col)
    if ch== True:
        mat,b=replacement(mat,row,b)
        typ,a=sol_check(mat,b,row)
        if typ==True:
            X=back_sub(mat,b,row,X)
            print('Solution is',X)
        else:
            print(a)
    else:
        print('Sorry')
elif row<col:
    Y=[0]*row
    B=mat_mul(mat,row,col)
    ch=check(B,row,col)
    if ch== True:
        B,b=replacement(B,row,b)
        typ,a=sol_check(B,b,row)
        if typ==True:
            z=[[0]*1]*row
            Y=back_sub(B,b,row,Y)
            for n in range(len(Y)):
                z[n][0]=Y[n]
            X=matrix_m(trp(mat),z)
            print('Solution is',X)
        else:
            print(a)
    else:
        print('Sorry')##need robust method
elif row>col:
    B=t_mat_mul(mat,row,col)
    ch=check(B,row,col)
    if ch== True:
        z=[[0]*1]*row
        for n in range(len(b)):
            z[n][0]=b[n]
        d=matrix_m(trp(mat),z)
        B,d=replacement(B,col,d)
        typ,a=sol_check(B,b,col)
        if typ==True:
            X=back_sub(B,d,col,X)
            print('Solution is',X)
        else:
            print(a)
    else:
        print('Sorry')
q=str(input('Press enter to exit'))
