# -*- coding: utf-8 -*-
"""
Created on Sun May  4 16:56:28 2025

@author: 六町妖妖
"""

import pandas as pd
import numpy as np
from sympy import symbols, Matrix, prod, expand,Poly

# 定义符号变量
Y1, Y2, Y3, Y4 = symbols('Y1 Y2 Y3 Y4')
Z1, Z2, Z3, Z4 = symbols('Z1 Z2 Z3 Z4')
alpha, beta, g, eta,lambda_sym = symbols('alpha beta g eta lambda')
params = [alpha, beta, g, eta]
Y = [Y1, Y2, Y3, Y4]

# 读取Excel文件
df = pd.read_excel('valid_networks.xlsx')

# 处理每一行
for index, row in df.iterrows():
    # 解析Gamma, Gamma_l, u
    Gamma = np.array(eval(row['Γ'])).reshape(4,5)
    Gamma_l = np.array(eval(row['Γ_l'])).T
    u = np.array(eval(row['u'])).flatten()
    
    # 计算每个反应的速率项
    rates = []
    for i in range(5):
        exponents = Gamma_l[i,:]
        y_terms =[Y[j]**exponents[j] for j in range(4)]
        rate = u[i] * prod(y_terms)
        rates.append(rate)
    rates = np.array(rates)
    
    # 计算每个物种的动力学方程
    result = Gamma @ rates
    fY = []
    for i in range(4):
        equation = result[i] * params[i]
        fY.append(equation)
    df.at[index, 'fY'] =str(fY)
    # 坐标变换到Z变量（平移平衡点至原点）
    subs_dict = {Y1: Z1 + 1, Y2: Z2 + 1, Y3: Z3 + 1, Y4: Z4 + 1}
    fZ = [eq.subs(subs_dict) for eq in fY]
    fZ = [expand(eq) for eq in fZ]
    
    # 计算雅可比矩阵在原点处的值
    Z = [Z1, Z2, Z3, Z4]
    J = []
    for fi in fZ:
        row = []
        for z in Z:
            dfi_dz = fi.diff(z)
            dfi_dz_at0 = dfi_dz.subs({Z1:0, Z2:0, Z3:0, Z4:0})
            row.append(dfi_dz_at0)
        J.append(row)

    # 保存到DataFrame
    
    df.at[index, 'Jacobian']=str(J)
    
    # 计算特征多项式系数
    char_poly = Matrix(J).charpoly(lambda_sym)
    coeffs = char_poly.all_coeffs()
    co=[]
    a0, a1, a2, a3 = coeffs[-1], coeffs[-2], coeffs[-3], coeffs[-4]
    if a0!=0:# 对应常数项到高次项
        co.append([a0,a1,a2,a3])
        df.at[index,'系数']=str(co)
# 保存到新文件
df.to_excel('output_with_fY_and_Jacobian.xlsx', index=False)