#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:jinchen
Email:278229887@qq.com
data:11/11/2023 下午 3:51
"""
import pandas as pd

from Concurrent.fuzzy_match import FuzzyMatchV2


def get_fuzzy_much(a, key_str, key_list):
    if a!= -1:
        return '不需要模糊匹配'
    match_list = matcher.run(key_str, set(key_list))
    if match_list[0]:
        if match_list[0].get('match_ratio') < 0.4:  # 模糊匹配结果
            return '模糊匹配不到结果'
        return match_list[0].get('match_result')
    return '模糊匹配不到结果'


if __name__ == "__main__":
    df1 = pd.read_excel(r'C:\Users\27822\Desktop\投诉机构处理后1111-0925(1).xlsx')
    df2 = pd.read_excel(r'C:\Users\27822\Desktop\医疗机构名称+地址 (5).xlsx')
    match_answwer_list = df2.dropna(subset=['机构别名'])['机构别名'].to_list()

    matcher = FuzzyMatchV2(top_n=1)

    df1['fuzzy_match_answewr'] = df1.apply(lambda x: get_fuzzy_much(x['merge_index'],
                                                                    x['投诉机构'], match_answwer_list), axis=1)

    df = df1.merge(df2, left_on='fuzzy_match_answewr', right_on='机构别名', how='left')

    df.to_excel('fuzzy_match.xlsx')
    print('xx')
