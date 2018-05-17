import os
import subprocess
from questao1 import *

os.system("rpm -qa > installedPackages.txt")
packageList = open("installedPackages.txt").read()
if "bind" not in packageList:
        os.system("yum install bind *")

dominio_input = raw_input("Insira o dominio: ")

zone_forward = '\nzone "'+dominio_input+'" IN { \n	type master;\n	file "/var/named/'+dominio_input+'.hosts";\n};'

hosts_file = '$TTL 38400\n@	IN	SOA	trabalho.pt. mail.'+dominio_input+'.(\n			100;\n			10800;\n			3600;\n			684000;\n			38400;\n			)\n	IN	NS	trabalho.pt.\n	IN	A	127.0.0.1'

resolv_dns_file = "search trabalho.pt\nnameserver 127.0.0.1"

register_input = raw_input("Tipo de registo (A ou MX): ").upper()

def register_type(register):
	if register == 'MX':
   		host = '\n        IN      MX      10      smtp.'+dominio_input
	elif register == 'A':
		prefixo = raw_input("Insira o prefixo: ")
		ip = raw_input("Insira o IP: ")
		host = '\n'+prefixo+'	IN      A       '+ip
	with open("/var/named/"+dominio_input+".hosts", "a") as myfile:
		myfile.write(host)

def check_zone_create_register(zone):
	file = open("/etc/named.conf").read()
	if dominio_input in file:
		register_type(register_input)
	else:
		create_zone(zone_forward, dominio_input)
		create_hosts_file(dominio_input, hosts_file)
		register_type(register_input)
	restart_named()

replace_lines()
write_resolv_file(resolv_dns_file)
check_zone_create_register(zone_forward)

