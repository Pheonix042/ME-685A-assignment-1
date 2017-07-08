from operator import add,mul,sub
import numpy as nup
from math import sin,e,exp,sinh,cos,cosh,tan,tanh,pi,log,log10,log2,factorial,acos,asin,acosh,asinh,atan,atanh
def quad(a,b,c):
    from cmath import sqrt
    if a!=0:
        z1=add((-b),sqrt(sub(b**2,4*a*c)))/(2*a)
        z2=sub((-b),sqrt(sub(b**2,4*a*c)))/(2*a)
        
    else:
        z1=z2(-c/b)
    return z1,z2
def condition_no(name):
    from math import sqrt
    h=0.001
    f=[]
    fh=[]
    ab=[]
    conditi=[]
    x=list
    for x in nup.arange(-1,1.1,0.1):
        for y in nup.arange(-1,1.1,0.1):
            try:
                f.append(eval(name))
                ab.append(sqrt(add(x**2,y**2)))
            except ValueError:
                pass
    for x in nup.arange(-1,1.1,0.1):
        try:
            x=x+h
            for y in nup.arange(-1,1.1,0.1):
                try:
                    y=y+h
                    fh.append(eval(name))
                except ValueError:
                    pass
        except ValueError:
            pass
    for num in range(0,len(f)):
        if f[num]!=0:
            D=abs(f[num])*sqrt(2)*h
            N=abs(fh[num]-f[num])*ab[num]
            conditi.append(N/D)
        else:
            conditi.append(None)
    return conditi
def differential_1(name):
    h=0.001
    fp1=[]
    fp2=[]
    fn1=[]
    fn2=[]
    del1=[]
    del2=[]
    del3=[]
    for x in nup.arange(-1,1.1,0.1):
        try:
            x=x+h
            fp1.append(eval(name))
            x=x+h
            fp2.append(eval(name))
            x=x-4*h
            fn2.append(eval(name))
            x=x+h
            fn1.append(eval(name))
        except ValueError:
            pass
    for num in range(0,len(fp1)):
        del1.append((8*fp1[num] - 8*fn1[num] - fp2[num] + fn2[num])/(12*h))
        del3.append((fp2[num]- 2*fp1[num] + 2*fn1[num] -fn2[num])/(2*h**3))
        del2.append((fp2[num]+fn2[num]-fp1[num]-fn1[num])/(3*h**2))
    return del1,del2,del3
def check(A,row,col):
    for n in range(min(col,row)):
        rep=0
        for m in range(min(col,row)):
            if A[m][n]==0:
                rep+=1
            else:
                pass
        if rep==row:
            break
        else:
            pass
    if rep==row:
        return False
    else:
        return True
def interchange(A,b,row,num7):
    for num9 in range(num7+1,row):
        pii=A[num9][num7]
        for num10 in range(0,row):
            A[num9][num10]=A[num9][num10]-(pii*A[num7][num10]/A[num7][num7])
            if abs(A[num9][num10])<(1e-4):
                A[num9][num10]=0
        b[num9]=b[num9]-(b[num7]*pii/A[num7][num7])
        if abs(b[num9])<(1e-4):
            b[num9]=0
    return A,b
def replacement(A,row,b):
    for num7 in range(0,row):
        pip=abs(A[num7][num7])
        pivot=num7
        if num7!=(row-1):
            for num8 in range(num7,row):
                if abs(A[num8][num7])>pip:
                    pivot=num8
                    pip=A[num8][num7]
            A[pivot],A[num7]=A[num7],A[pivot]
            b[pivot],b[num7]=b[num7],b[pivot]
            A,b=interchange(A,b,row,num7)
        else:
            pass
    return A,b
def sol_check(A,b,row):
    if A[row-1][row-1]==0:
        if b[row-1]==0:
            a= 'infinite possible solution'
        else:
            a= 'no solution possible'
        return False,a
    else:
        a='Unique solution exist'
        return True,a
def back_sub(A,b,row,X):
    for num12 in range(row,0,-1):
        aa=0
        for num13 in range(num12,row):
            aa=aa-X[num13]*A[num12-1][num13]
        X[num12-1]=(b[num12-1]+aa)/A[num12-1][num12-1]
    return X
def trp(A):
    A_T=[]
    for num14 in zip(*A):
        A_T.append(num14)
    return A_T
def mat_mul(A,row,col):
    at=trp(A)
    aat=[[0 for col in range(len(at[0]))] for row in range(len(A))]
    for num16 in range(row):
        for num17 in range(row):
            for num18 in range(col):
                aat[num16][num17]+=A[num16][num18]*at[num18][num17]
    return aat
def matrix_m(A,Y):
    zA=nup.matrix(A)
    zY=nup.matrix(Y)
    anm=zA * zY
    return anm
def t_mat_mul(A,row,col):
    at=trp(A)
    aat=[[0 for col in range(len(A[0]))] for row in range(len(at))]
    for num16 in range(col):
        for num17 in range(col):
            for num18 in range(row):
                aat[num16][num17]+=A[num18][num17]*at[num16][num18]
    return aat
