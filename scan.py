# https://nmap.org/    ------> install nmap
# https://npcap.com/download   ------> install npcap
import nmap
ip=input("Please enter your ip")
if len(ip)==0 :
    network="192.168.1.1/24"  #default if user don't input anything
else:
    network=ip+"/24"
nm=nmap.PortScanner()
nm.scan(hosts=network,arguments="-sL")
# hosts_list=[(x,nm[x]['status']['state']['hostname']) for x in nm.all_hosts()]
# for host,status in hosts_list:
#     print(f"hosts--->{host} ")
# print(hosts_list)
hostnames = []
hosts=[]
for host in nm.all_hosts():
    if 'hostname' in nm[host]:
        hostnames.append(nm[host]['hostname'])
    else:
        hosts.append(host)
print(hostnames)
print(host)