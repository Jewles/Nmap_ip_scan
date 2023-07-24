import sys
import nmap
import os

def scan_ips():
    s = nmap.PortScanner()
    s_all = nmap.PortScanner()
    ip_seg = input("IP Address:")
    s.scan(hosts=ip_seg, arguments='-n -sP')
    s_all.scan(hosts=ip_seg, arguments='-n -sL')

    s_fail = list(set(s_all.all_hosts()) - set(s.all_hosts()))

    print("该段IP地址总数:\n", len(s_all.all_hosts()))
    print("存活_IP总数：\n", len(s.all_hosts()))
    print("不在线_IP总数:\n", len(s_fail))

    print("存活IP列表：\033[1;32m")
    for upip in s.all_hosts():
        print(upip)
    print("\033[0m不在线IP列表：\033[1;31m")
    for noip in s_fail:
        print(noip)

if __name__ == "__main__":
    while True:
        scan_ips()
        restart = input("\033[1;33m继续扫描输入yes，关闭程序输入no(yes/no)：")
        if restart.lower() != "yes":
            sys.stdout.flush()
            sys.stderr.flush()
            os._exit(0)
