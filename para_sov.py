import numpy as np
from scipy.optimize import minimize
from objective1 import objective1
from objective2 import objective2
from sympy import Matrix, symbols

def solve(a_val):
    alpha, beta, g, eta ,w= symbols('alpha beta g eta w')
    def fun1(x):
        param_values = {alpha: x[0], beta: x[1], g: x[2], eta: x[3],w: x[4]}
        a = a_val.subs(param_values)
        value1 = objective1(x,a)
        return value1

    def fun2(x):
        param_values = {alpha: x[0], beta: x[1], g: x[2], eta: x[3],w: x[4]}
        a = a_val.subs(param_values)
        value2 = objective1(x,a)
        return value2   

    def min2(x):
        param_values = {alpha: x[0], beta: x[1], g: x[2], eta: x[3],w: x[4]}
        a = a_val.subs(param_values)
        value1 = objective1(x,a)
        value2 = objective2(x,a)
        #print(f"value1 类型: {type(value1)}, 值: {value1}")
        return value1 ** 2+value2**2
    
    w0=0.2
    # 设置变量边界（正实数）
    bounds = bounds = [(0.1, None)] * 4 + [(w0,None)] 

    # 使用随机初始猜测进行多次尝试
    np.random.seed(42)  # 固定随机种子以确保可重复性
    found = False
    f1_=0
    f2_=0
    for i in range(100):
        x0 = np.concatenate([
            np.random.uniform(0, 80.0, size=4),  # 前4个变量
            np.random.uniform(0, 20.0, size=1)  # 第5个变量
        ]) # 生成随机初始值
        res = minimize(min2, x0, method='L-BFGS-B', bounds=bounds, options={'maxiter': 10000, 'ftol': 1e-8})
        f1=fun1(res.x)
        f2=fun2(res.x)
        d_f1=f1-f1_
        d_f2=f2-f2_
        print("尝试次数：",i,"误差1:",f1,"误差2:",f2,"取值：",res.x)
        if res.success and abs(f1) < 1e-6 and abs(f2)<1e-6:
            found = True
            return res.x
        elif d_f1+d_f2==0 and res.x[4]==w0:
            break
        else:
            f1_=f1
            f2_=f2

    if not found:
        #print("未找到解，请尝试更多次迭代或调整初始范围。")
        return [0,0,0,0,0]