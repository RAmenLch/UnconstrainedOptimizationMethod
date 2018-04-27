import numpy as np
import numpy.linalg as LA
import sys
#添加一维搜索的模块
sys.path.append('..')
#进退法
from One_dimensional_search.AdvanceRetreatMethod import AR
#黄金分割法
from One_dimensional_search.GoldenSectionMethod import GSM
#f为正定二次函数
def fletcherReevesM(f,df,x0):
    xk = x0
    n = xk.shape[1]
    e = 10**-6
    d = -df(xk)
    k = 1
    while LA.norm(df(xk),2) > e :
        fdld = lambda ld:f(xk+ld*d)
        inv = AR(fdld)
        ld = GSM(fdld,inv)
        xk1 = xk + ld * d
        if k == n:
            xk = xk1
            d = -df(xk)
            k = 1
        else:
            beta = df(xk1).T * (df(xk1) - df(x)) / (df(xk).T * df(xk))
            d = -df(xk1) + beta * d
            xk = xk1
            k = k + 1
    return xk

if __name__ == '__main__':
    def f(x):
        x1 = float(x[0])
        x2 = float(x[1])
        x3 = float(x[2])
        return x1**2 -2*x1*x2 + 2*x2**2 + x3**2 - x1*x3 + x1 + 3*x2 - x3
    def df(x):
        x1 = float(x[0])
        x2 = float(x[1])
        x3 = float(x[2])
        return np.mat([ 2*x1 - 2*x2 - x3 + 1 , -2*x1 + 4*x2 + 3 , -x1 + 2*x3 - 1 ]).T
    xn = fletcherReevesM(f,df,np.mat([0,0,0]).T)
    #print(xn)
