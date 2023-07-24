import nmap

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

    print("\033[1;32m存活IP列表：")
    for upip in s.all_hosts():
        print(upip)
    print("\033[1;31m不在线IP列表：")
    for noip in s_fail:
        print(noip)

if __name__ == "__main__":
    while True:
        scan_ips()
        restart = input("是否扫描其他地址(yes/on)：")
        if restart.lower()!= "yes":
            break
