
import nmap

s = nmap.PortScanner()
s_all = nmap.PortScanner()
ip_seg = input("IP Address:")
s.scan(hosts=ip_seg, arguments='-n -sP')
s_all.scan(hosts=ip_seg, arguments='-n -sL')

print("IP_段总数:\n", len(s_all.all_hosts()))
print("存活_IP总数：\n", len(s.all_hosts()))
print("存活_IP List：\n", s.all_hosts())


s_fail = list(set(s_all.all_hosts()) - set(s.all_hosts()))
print("不在线_IP总数:\n", len(s_fail))
print("不在线_IP List：\n", s_fail)