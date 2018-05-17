import os
import subprocess
import string 
from questao1 import *

def delete_zone(dominio):
    fin = open("/etc/named.conf", "r")
    data = fin.readlines()
    fin.close()

    for i, line in enumerate(data):
            if dominio in line:
                del data[i:i+4]

    fout =open("teste.txt", "w")
    fout.writelines(data)
    fout.close()

def delete_virtualHost(ip_virtual_host):
    fin = open("/etc/httpd/conf/httpd.conf", "r")
    data = fin.readlines()
    fin.close()

    for i, line in enumerate(data):
            if ip_virtual_host in line:
                del data[i:i+6]

    fout =open("/etc/httpd/conf/httpd.conf", "w")
    fout.writelines(data)
    fout.close()

resposta_input = raw_input("Pretende eliminar o que?(1-zona forward /n 2-virtualhost /n 3-zona reverse):")

if resposta_input =="1":
    zona_forward = raw_input("Qual o nome da zona forward?")
    delete_zone(zona_forward)   
    os.system("rm /var/named/"+zona_forward+".hosts")

elif resposta_input =="2":
    dominio_virtual = raw_input("Qual o nome do dominio de VirtualHost que pretende eliminar?")
    ip_virtual = raw_input("Qual o Ip do VirtualHost que pretende eliminar?")
    delete_zone(dominio_virtual)
    os.system("rm /var/named/"+dominio_virtual+".hosts")
    delete_virtualHost(ip_virtual)
    os.system("rmdir /"+dominio_virtual)

elif resposta_input =="3":
    ip_reverse = raw_input("Qual o ip da zona reverse?")

    delete_zone(ip_reverse)
    os.system("rm /var/named/"+ip_reverse+".in-addr.arpa.hosts")
