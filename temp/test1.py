import configparser
import datetime
import json
import os
import re
from multiprocessing.dummy import Pool

import requests
from bs4 import BeautifulSoup

conf = """[host]
host_ip = 192.168.0.103
host_ref = /report

[user]
login_ref = /login/ajax/
name = ionadmin
pass = ionadmin

[bam]
bam_ext = /bam
counts = 1000
"""


def get_session_id(ip, login_ref, username="ionadmin", password="ionadmin"):
    req = requests.session()
    headers = {
        'Host': ip,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest'
    }
    login_url = "http://{}{}".format(ip, login_ref)
    payload = {
        "username": username,
        "password": password
    }
    result = req.post(login_url, data=payload, headers=headers)

    return result.cookies.get("sessionid")


def get_report_url(ip, ref, session_id):
    headers = {
        'Host': ip,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Cookie': 'sessionid={}'.format(session_id)
    }
    info_url = "http://{}{}".format(host_ip, ref)
    req = requests.session()
    result = req.get(info_url, headers=headers)
    soup = BeautifulSoup(result.text, "lxml")
    title = soup.title.string.strip().split()[0]
    p = re.compile('[0-9]+')
    return "{}_{}".format(title, re.findall(p, ref)[0])


def get_bam_list(ip, url, session_id):
    headers = {
        'Host': ip,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Cookie': 'sessionid={}'.format(session_id)
    }
    req = requests.session()
    result = req.get("{}/datasets_basecaller.json".format(url), headers=headers).text
    # 返回reads数大于1000的所有bam文件及对应链接
    return [
        ("{}/{}".format(url, i['basecaller_bam']), i['dataset_name'].split("/")[0].replace("-", "_").replace(" ", "_"),
         ip, session_id)
        for i in json.loads(result)["datasets"] if i["read_count"] >= min_counts]


def download_file(item):
    local_filename = "{}/{}.bam".format(dest_dir, item[1])
    # NOTE the stream=True parameter
    headers = {
        'Host': item[2],
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Cookie': 'sessionid={}'.format(item[3])
    }
    print("{} 开始下载".format(local_filename))
    req = requests.session()
    r = req.get(item[0], stream=True, headers=headers)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                # f.flush() commented by recommendation from J.F.Sebastian
    print("{} 下载完成".format(local_filename))
    return local_filename


if __name__ == "__main__":
    conf_file = "config.ini"
    if not os.path.exists(conf_file):
        with open(conf_file, "w") as fh:
            fh.write(conf)

    print("佰美基因数据中心计算部")
    print("16s BAM文件下载器")
    print("\t\tby ferstar")
    report_id = input("请输入样本报告id: ")
    while not report_id.isdigit():
        report_id = input("格式有误, 请重新输入样本报告id: ")

    cf = configparser.ConfigParser()
    cf.read(conf_file)

    host_ip = cf.get("host", "host_ip")
    report_ref = "{}/{}/".format(cf.get("host", "host_ref"), report_id)
    login_ref = cf.get("user", "login_ref")
    username = cf.get("user", "name")
    password = cf.get("user", "pass")
    bam_ext = cf.get("bam", "bam_ext")
    min_counts = cf.getint("bam", "counts")

    dest_dir = datetime.datetime.now().strftime("%Y%m%d%H%M") + bam_ext
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    session_id = get_session_id(host_ip, login_ref, username, password)
    # print(session_id)
    reports = get_report_url(host_ip, report_ref, session_id)
    # print(reports)
    report_url = "http://{}/output/Home/{}/basecaller_results".format(host_ip, reports)
    lst = get_bam_list(host_ip, report_url, session_id)
    pool = Pool()
    pool.map(download_file, lst)
    pool.close()
    pool.join()
    input("下载完成, 按回车键退出")
