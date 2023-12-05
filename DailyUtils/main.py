#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:jinchen
Email:278229887@qq.com
date:17/11/2023 上午 9:40
"""
import builtins

import requests
import pandas as pd
from multiprocessing.dummy import Pool as ThreadPool
import pymssql
from sqlalchemy import create_engine

from TransformLatitude.utils import gcj02_to_wgs84


class FindGPS:
    def __init__(self):
        self.ak = 'aa78ccfd6fbf247a4c770a5aa758f729'
        self.url_string = None
        self.pd_in = None
        self.sel_col = None
        self.pd_out = pd.DataFrame()
        self.row_num = 0
        self.in_api_type = 'gaode'
        self.out_gps_format = 'wgs84'
        self.p_c = None

    def access_one(self, in_data):
        add_in, main_id = in_data
        if self.in_api_type == 'gaode':
            self.url_string = 'https://restapi.amap.com/v3/geocode/geo?address=' \
                              '{0}&output=JSON&key={1}'.format(add_in, self.ak)
        a_row_dict_na = {
            'address_in': add_in,
            'formatted_address': '没找到',
            'adcode': '没找到',
            'city': '没找到',
            'district': '没找到',
            'level': '没找到',
            'lng_GCJ02': 0,
            'lat_GCJ02': 0,
            'main_id': main_id,
        }
        try:
            wb_data_org = requests.get(self.url_string, headers={'Connection': 'close'}, timeout=500).json()
        except:
            self.row_num = self.row_num + 1
            a_row_dict = a_row_dict_na
            a_row_dict['formatted_address'] = '请求错误'
            return a_row_dict

        if wb_data_org['status'] == '1':  # 请求成功
            self.row_num = self.row_num + 1
            try:
                a_row = wb_data_org['geocodes'][0]
                location = a_row['location'].split(',')
                lng = location[0]
                lat = location[1]
                a_row_dict = {
                    'address_in': add_in,
                    'formatted_address': a_row['formatted_address'],
                    'adcode': a_row['adcode'],  # 区域编码
                    'city': a_row['city'],  # 城市
                    'district': a_row['district'],  # 区
                    'level': a_row['level'],
                    'lng_GCJ02': lng,
                    'lat_GCJ02': lat,
                    'main_id': main_id,
                }
            except:
                a_row_dict = a_row_dict_na
        else:
            self.row_num = self.row_num + 1
            a_row_dict = a_row_dict_na

        if self.out_gps_format == 'wgs84':
            a_row_dict['gps_type'] = 'wgs84'
            temp_gps = gcj02_to_wgs84(float(a_row_dict['lng_GCJ02']),
                                      float(a_row_dict['lat_GCJ02']))
            a_row_dict['lng_out'] = str(temp_gps[0])
            a_row_dict.pop('lng_GCJ02')
            a_row_dict['lat_out'] = str(temp_gps[1])
            a_row_dict.pop('lat_GCJ02')

        return a_row_dict


class Find_GPS:
    def __init__(self, file_in_path, file_out_name, col_name):
        self.file_path = file_in_path
        self.file_out_name = file_out_name
        self.col_name = col_name
        self.out_df = None
        self.out_path = None

    def run(self, ThreadPool_num=10):
        findGPS = FindGPS()
        findGPS.open_a_col(self.file_path, self.col_name)
        data_in = findGPS.sel_col.tolist()
        data_out = pd.DataFrame()
        requests.adapters.DEFAULT_RETRIES = 5
        for i in range(0, len(data_in), ThreadPool_num * 5):
            chunk = data_in[i:i + ThreadPool_num * 5]
            pool = ThreadPool(ThreadPool_num)  # 创建线程池并发执行
            ret = pool.map(findGPS.access_one, chunk)
            data_out_a = findGPS.pd_out.append(ret)
            pool.close()
            pool.join()
            data_out = data_out.append(data_out_a)
        findGPS.pd_out = data_out
        findGPS.write(self.file_out_name)
        self.out_path = findGPS.p_c
        self.out_df = data_out

    def single_run(self):
        findGPS = FindGPS()
        findGPS.open_a_col(self.file_path, self.col_name)
        data_in = findGPS.sel_col.tolist()
        data_out = pd.DataFrame()
        ret = list(map(findGPS.access_one, data_in))
        data_out_a = findGPS.pd_out.append(ret)
        data_out = data_out.append(data_out_a)
        findGPS.pd_out = data_out
        findGPS.write(self.file_out_name)
        self.out_path = findGPS.p_c
        self.out_df = data_out
        self.out_name = data_out



if __name__ == "__main__":

    # df1 = pd.read_csv(r'C:\Users\27822\Desktop\2016_西医.csv')
    # df1 = df1.iloc[2813262:2989260, :]
    # data_in = df1[['现住址', 'mainid']].to_records(index=False)
    # findGPS = FindGPS()
    # ThreadPool_num = 10
    # data_out = pd.DataFrame()
    # for i in range(0, len(data_in), ThreadPool_num * 5):
    #     chunk = data_in[i:i + ThreadPool_num * 5]
    #     pool = ThreadPool(ThreadPool_num)  # 创建线程池并发执行
    #     ret = pool.map(findGPS.access_one, chunk)
    #     data_out_a = findGPS.pd_out.append(ret)
    #     pool.close()
    #     pool.join()
    #     data_out = data_out.append(data_out_a)
    # df = df1.merge(data_out, left_on='mainid', right_on='main_id', how='left')
    # df.to_csv('2016_西医缺_地址.csv', index=False)
    path = r'C:\Users\27822\Documents\WeChat Files\wxid_dk7z6sy2eek622\FileStorage\File\2023-11\PSU.dta'
    # df = data = pd.read_stata(path, encoding='utf-8')
    df = pd.read_stata(path, encoding='UTF-8')
    print('sss')