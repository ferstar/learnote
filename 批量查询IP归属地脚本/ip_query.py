#!/usr/bin/env python
# coding='utf-8'

"""Query IP from taobao ip API
via <http://ip.taobao.com>
Usage:
    ip_query.py [-i=in] [-o=out] [-v]
    ip_query.py -h | --help | --version
Options:
    -h --help   show this help message and exit
    --version   show version and exit
    -i in       file that has ip each line [default: ips.txt]
    -o out      output file name(with 'csv' format) [default: out.csv]
    -v          explain what is being done
"""

import json
import os
import sys

import pandas as pd
import requests
from docopt import docopt


def query_ip(ip):
    url = "http://ip.taobao.com/service/getIpInfo.php"
    querystring = {
        "ip": ip
    }
    headers = {
        'cache-control': "no-cache",
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    result = json.loads(response.text)
    if result['code'] == 0:
        return result['data']
    else:
        return {
            "country": result['data'],
            "country_id": "",
            "area": "",
            "area_id": "",
            "region": "",
            "region_id": "",
            "city": "",
            "city_id": "",
            "county": "",
            "county_id": "",
            "isp": "",
            "isp_id": "",
            "ip": ""
        }


def get_ip_pool(ip_file):
    with open(ip_file, 'r') as fh:
        ip_pool = {}
        while 1:
            line = fh.readline()
            if not line:
                break
            ip = line.rstrip()
            if ip_pool.get(ip):
                ip_pool[ip]['count'] += 1
            else:
                ip_pool[ip] = {
                    'count': 1
                }
    return ip_pool


def main(fp, csv_file):
    ips = get_ip_pool(fp)
    for ip, data in ips.items():
        data.update(query_ip(ip))
        if arguments['-v']:
            print(data)
    df = pd.DataFrame.from_dict(ips, orient='index').sort_values(by='count', ascending=False)[
        ['count',  # 计数
         'country',  # 国家
         'isp',  # 运营商
         'area',  # 区域
         'region',  # 省
         'city',  # 城市
         'county'  # 县/区
         ]
    ]
    with open(csv_file, 'w') as fh:
        df.to_csv(fh, index_label='ip')


if __name__ == "__main__":
    arguments = docopt(__doc__, version='Query IP 1.0')
    in_fp, out_fp = arguments['-i'], arguments['-o']
    if os.path.exists(in_fp):
        main(in_fp, out_fp)
    else:
        sys.exit("the file '{}' does not exist".format(in_fp))
