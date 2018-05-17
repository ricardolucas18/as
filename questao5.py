import os
import subprocess
import string 
from questao1 import *

os.system("rpm -qa > installedPackages.txt")
packageList = open("installedPackages.txt").read()
if "bind" not in packageList:
	os.system("yum install bind *")

gama_ip = raw_input("Insira o IP para a zona reverse: ")
fqdn = raw_input("Insira o FQDN: ")
ip = raw_input("Insira o IP para o FQDN: ")

zone = 'zone "'+gama_ip+'.in-addr.arpa" IN { \n	type master;\n	file "/var/named/reverse.'+fqdn+'";\n};'

reverse = '$TTL 38400\n@	IN	SOA	@ root(\n			100;\n			10800;\n			3600;\n			684000;\n			38400;\n			)\n	IN	NS	trabalho.pt.\n'+ip+'	IN	PTR	'+fqdn+'.\n'

resolv_dns = "search trabalho.pt\nnameserver 127.0.0.1"

with open("/var/named/reverse."+fqdn, "w") as myfile:
	myfile.write(reverse)

file = open("/etc/named.conf").read()
if gama_ip not in file:
	create_zone(zone, gama_ip)

write_resolv_file(resolv_dns)
replace_lines()

subprocess.check_call("service named restart".split())

