import multiprocessing
import pandas as pd
import re
import numpy as np


class FullSerchInstitution:
    def __init__(self, data):
        self.data = data
        self.info_list1 = data['机构名'].to_list()
        self.info_list2 = data['地址'].to_list()
        self.info_list3 = data['机构别名'].to_list()

    @classmethod
    def formatdata(cls, path):
        df = pd.read_excel(path)
        df.dropna(subset=['机构名', '地址'], inplace=True)
        df['地址二'] = df['地址'].map(lambda x: '空' if pd.isna(x) else x)
        df['别名'] = df['机构别名'].map(lambda x: '空' if pd.isna(x) else x)
        df_ins = df.groupby(['机构名', '地址二']).apply(cls.get_zip_info)
        df_ins.reset_index(drop=True, inplace=True)
        df_ins['index'] = df_ins.index
        return cls(df_ins)

    def run(self, df):
        print('任务开始')
        df['is_number'] = df['投诉机构'].map(lambda x: self.is_legal_name(x))  # 是否合法名称
        df['merge_index'] = df.apply(lambda x: self.get_info_v2(x['投诉机构'], x['是否排除'], x['is_number']), axis=1)  # 输出匹配索引
        df = df.merge(self.data, left_on='merge_index', right_on='index', how='left')  # 合并信息

        conditions = [
            df['merge_index'] == -3,
            df['merge_index'] == -1,
            df['merge_index'] == -2
        ]

        choices = [
            '名称不合法',
            '找不到',
            '其他'
        ]

        df['final_name'] = np.select(conditions, choices, default=df['机构名'])

        print('任务结束')
        return df

    @staticmethod
    def get_zip_info(x):
        return pd.DataFrame([{
            '机构名': x.iloc[0, 0],
            '地址': x.iloc[0, 1],
            '机构别名': '#'.join(x['别名'].to_list()),
        }])

    def get_info_v2(self, x, y, z):
        if y == '排除': return -2  # 被排除
        if z == '不合法': return -3  # 名称不合法

        for i in self.info_list1:
            if pd.isna(i):
                continue
            if i in x:
                index = self.data[self.data['机构名'] == i]['index'].to_list()[0]
                return index
        for t in self.info_list2:
            if t in x:
                index = self.data[self.data['地址'] == t]['index'].to_list()[0]
                return index
        for m in self.info_list3:
            m_list = m.split('#')
            if m_list[0] == '空':
                continue
            for m_s in m_list:
                if m_s in x:
                    index = self.data[self.data['机构别名'] == m]['index'].to_list()[0]
                    return index
        return -1  # 未找到

    @staticmethod
    def is_legal_name(x):
        zhmodel = re.compile(u'[\u4e00-\u9fa5]')  # 检查中文
        match = zhmodel.search(x)
        if not match:
            return '不合法'
        return ''


if __name__ == '__main__':
    # 原始数据
    df1 = pd.read_excel(r'C:\Users\27822\Desktop\11\投诉机构.xlsx')
    df3 = pd.read_excel(r'C:\Users\27822\Desktop\11\划掉名单.xlsx')
    exclude_list = df3['投诉机构'].to_list()
    df1['是否排除'] = df1['投诉机构'].map(lambda x: '排除' if x in exclude_list else '')  # 如果在投诉
    df1.dropna(subset=['投诉机构'], inplace=True)

    file_path = r'C:\Users\27822\Desktop\11\医疗机构.xlsx'
    MyProcess = FullSerchInstitution.formatdata(path=file_path)

    # 主表分块多进程操作
    chunk_size = 10000
    data = np.array_split(df1, len(df1) // chunk_size)

    # 创建进程池，指定进程数量
    num_processes = 6  # 使用 CPU 核心数作为进程数量
    pool = multiprocessing.Pool(processes=num_processes)

    # 使用进程池处理数据
    results = pool.map(MyProcess.run, data)

    # 关闭进程池

    pool.close()
    pool.join()

    # 处理结果
    df_final = pd.concat(results)
    df_final.to_excel('tttttt.xlsx', index=False)
    print('结束')
