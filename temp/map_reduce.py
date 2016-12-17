import configparser
import os

if not os.path.exists("config.ini"):
    with open("config.ini", "w") as fh:
        fh.write(
            """[host]
host_ip = 192.168.0.103
host_ref = /report

[user]
name = ionadmin
pass = ionadmin

[bam]
bam_ext = bam
counts = 1000
"""
        )

cf = configparser.ConfigParser()
cf.read("config.ini")

host_ip = cf.get("host", "host_ip")
host_ref = cf.get("host", "host_ref")
username = cf.get("user", "name")
password = cf.get("user", "pass")
bam_ext = cf.get("bam", "bam_ext")
min_counts = cf.getint("bam", "counts")

print(host_ip)
print(host_ref)
print(username)
print(password)
print(bam_ext)
print(min_counts)