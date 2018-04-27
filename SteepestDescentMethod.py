import numpy as np
import numpy.linalg as LA
import sys
#添加一维搜索的模块
sys.path.append('..')
#进退法
from One_dimensional_search.AdvanceRetreatMethod import AR
#黄金分割法
from One_dimensional_search.GoldenSectionMethod import GSM

#f为凸规划.求最小点
def sdmMin(f,dltf,x0):
    x = x0
    e = 10**-8
    c = 0
    while(c <= 100):
        #定理5-4,P112
        normdfx =  LA.norm(dltf(x),2)
        if normdfx < e:
            break
        else:
            d = -dltf(x)
            fdld = lambda ld:f(x+ld*d)
            inv = AR(fdld)
            ld = GSM(fdld,inv)
            x = x + ld * d
        c+=1
    return x

def f(x):
    return  float(x.T * np.mat([[3,0],[0,3]])*x + np.mat([2,-4])*x)

def df(x):
    x1,x2 = x.tolist()
    x1 = x1[0]
    x2 = x2[0]
    return np.mat([6*x1+2,6*x2-4]).T



x = sdmMin(f,df,np.mat([1,1]).T)
print(x)
