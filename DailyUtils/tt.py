#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:jinchen
Email:278229887@qq.com
date:22/11/2023 上午 10:20
"""

import os
import pandas as pd


def get_files(path):
    for filepath, _, filenames in os.walk(path):
        for filename in filenames:
            if '-' in filename:
                file_name = filename.replace('.xlsx', '')
                file_name_list = file_name.split('-')
                for f in file_name_list:
                    if "院" in f or '中心' in f:
                        file_name = f
            else:
                file_name = filename.split('.')[0]
            file_path = os.path.join(filepath, filename)
            file_info.append((file_name, file_path))
            file_name_total.append(file_name)


file_name_total = []
file_info = []
path = r'C:\Users\27822\Desktop\电子病历测评'
get_files(path=path)

df_function_list = []
error_list = []
for i in file_info:
    name, path = i
    # try:
    df = pd.read_excel(path, sheet_name="有效应用", dtype=str)
    df['子项分数小于1'] = df['有效应用评分'].map(lambda x: '满足' if float(x) == 1 else '不满足')
    df['ins_name'] = name
    df_function_list.append(df)
    # except:
    #     error_list.append(path)
df_function_total = pd.concat(df_function_list)
df_function_total.dropna(subset='项目代码', inplace=True)

df_function_des = df_function_total.groupby(['项目代码','子项分数小于1'])['ins_name'].count()
df_function_des = pd.DataFrame(df_function_des)
df_function_des.reset_index(inplace=True)
df_function_des.to_excel('有效应用评测统计.xlsx')

# print("VsCode")
print(len(df_function_list))
print(len(file_name_total))
print(error_list)


# a="'角色','项目代码','评价类别', '业务项目','评价特性',
#                                             '数据元名称'"