import pandas as pd
import numpy as np
from objective1 import objective1
from objective2 import objective2
from para_sov import solve
from openpyxl import load_workbook
import re
from sympy import Matrix, symbols

# 读取文件
excel_file = pd.ExcelFile('output_with_fY_and_Jacobian.xlsx')
# 获取指定工作表中的数据
df = excel_file.parse('Sheet1')

# 提取parameters列的值，并去除缺失值
parameters_values = df['系数'].dropna()
# 创建空列表用于存储解析后的值
A = []
results_list=[]
alpha, beta, g, eta = symbols('alpha beta g eta')

for value in parameters_values:
    # 使用正则表达式去除方括号
    expressions = value.strip('[]').split(', ')
    # 解析当前行数据
    row = Matrix([eval(expr) for expr in expressions])
    # 添加当前行到矩阵
    A.append(row)

# 示例调用，这里假设alpha=1, beta=2, g=3, eta=4
for i, a in enumerate(A, start=1):
    result=solve(a)
    print("找到一组正实数解：", result,"i=",i)
    results_list.append(', '.join(map(str, result)))

# 将结果列表添加为新列
df['result'] = results_list

# 保存到新的 Excel 文件
df.to_excel('result2.xlsx', index=False)