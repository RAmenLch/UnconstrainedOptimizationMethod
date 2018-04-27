import numpy as np
import numpy.linalg as LA
import sys

#牛顿法
def NtM(df,ddf,x0):
    x = x0
    e = 10**-8
    while(1):
        dfx = df(x)
        ddfx = ddf(x)
        s = ddfx.I * (-dfx)
        x = x + s
        if LA.norm(s,2) < e:
            break
    return x

if __name__ == '__main__':
    def f(x):
        x1 = float(x[0])
        x2 = float(x[1])
        return 2*x1**4 - 3*x1**2 + 2*x2**2 +2*x1*x2 - 3*x1 - 4*x2
    def df(x):
        x1 = float(x[0])
        x2 = float(x[1])
        dfx1 = 8*x1**3 - 6*x1 + 2*x2 -3
        dfx2 = 4*x2 + 2*x1 - 4
        return np.mat([dfx1,dfx2]).T
    def ddf(x):
        x1 = float(x[0])
        x2 = float(x[1])
        ddfx11 = 24*x1**2 - 6
        ddfx12 = 2
        ddfx21 = 2
        ddfx22 = 8
        return np.mat([[ddfx11,ddfx12],[ddfx21,ddfx22]])
    xn = NtM(df,ddf,np.mat([1,1]).T)
    print(xn)
