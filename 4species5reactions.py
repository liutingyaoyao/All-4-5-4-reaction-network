# -*- coding: utf-8 -*-
"""
Created on Sun May  4 00:03:26 2025

@author: 六町妖妖
"""

import numpy as np
import pandas as pd
from itertools import product
import random
from sympy import Matrix

def generate_gamma_columns():
    """生成所有可能的有效Γ列（每个反应的变化）"""
    columns = []
    for gamma in product([-1, 0, 1], repeat=4):
        gamma = np.array(gamma)
        if np.all(gamma == 0):
            continue
        # 检查是否存在非零的r
        r = np.zeros(4, dtype=int)
        valid = False
        for i in range(4):
            if gamma[i] == 1:
                r[i] = 0
            elif gamma[i] == -1:
                r[i] = 1
            else:
                r[i] = 0  # 暂定，后续需要验证r非零
        # 生成可能的所有r（考虑gamma=0的位置可以是0或1）
        # 此处简化：仅处理gamma含非零元素的情况
        if np.any(r != 0) or np.any(gamma != 0):
            columns.append(gamma)
    return columns

def is_valid_network(gamma_matrix, gamma_l):
    """检查Γ的秩为4且满足ND条件"""
    if np.linalg.matrix_rank(gamma_matrix) != 4:
        return False
    gamma_l_t= gamma_l.T
    augmented = np.c_[gamma_l,np.array([-1,-1,-1,-1,-1]).T]
    return np.linalg.matrix_rank(augmented) == 5

# 生成所有可能的Γ列并采样组合
gamma_columns = generate_gamma_columns()
print(f"共有 {len(gamma_columns)} 种可能的Γ列")

networks = []
attempts = 1000  # 调整尝试次数以平衡计算时间

for _ in range(attempts):
    # 随机选择5个Γ列
    selected = random.sample(gamma_columns, 5)
    gamma_matrix = np.column_stack(selected)
    # 生成对应的Γ_l（假设每个Γ列对应一个r）
    gamma_l = []
    for col in selected:
        r = np.where(col == 1, 0, np.where(col == -1, 1, 0))
        gamma_l.append(r)
    gamma_l = np.array(gamma_l)
    if is_valid_network(gamma_matrix, gamma_l)==True:
        u= Matrix(gamma_matrix).nullspace()
        u= np.array(u).reshape(-1)

        networks.append({
            "Γ": gamma_matrix.tolist(),
            "Γ_l": gamma_l.tolist(),
            "u":u.tolist()
        })

# 保存到Excel
df = pd.DataFrame(networks)
df.to_excel("valid_networks.xlsx", index=False)
print(f"找到 {len(networks)} 个有效网络，已保存到 valid_networks.xlsx")