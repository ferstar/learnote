#!/usr/bin/env python
# coding='utf-8'
import json
import sys

import pandas as pd
import requests


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
    df = pd.DataFrame.from_dict(ips, orient='index').sort_values(by='count', ascending=False)[
        ['count',
         'country',
         'isp',
         'area',
         'region',
         'city',
         'county'
         ]
    ]
    with open(csv_file, 'w') as fh:
        df.to_csv(fh, index_label='ip')


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit('Usage: {} <ip_file> <out_csv_file>'.format(sys.argv[0]))
    else:
        main(sys.argv[1], sys.argv[2])
