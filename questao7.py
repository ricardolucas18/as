import os
import subprocess
import string 
from questao1 import *

os.system("rpm -qa > installedPackages.txt")
pacotesInstalados = open("installedPackages.txt").read()
if "nfs" not in pacotesInstalados:
	os.system("yum install nfs*")


def exportsConfig(diretoria):
    ip_network = raw_input("Qual o ip da network?(ex: 192.168.43.0/24\n")
    optionsRead = raw_input("Options:\n1-Read and Write Acess.\n2-Read Only Acess.\n")
    
    if optionsRead =="1":
        optionOne = "rw"
    elif optionsRead =="2":
        optionOne = "ro"
 
    optionsWrites = raw_input("Options:\n1-Writes Data when the server feels the need, not the client.\n2-Writes data as it is received.\n")
    if optionsWrites =="1":
        optionTwo = "async"
    elif optionsWrites =="2":
        optionTwo = "sync"


    optionsHide = raw_input("Options:\n1-hide\n2-no hide\n")
    if optionsHide =="1":
        optionThree = "hide"
    elif optionsHide =="2":
        optionThree = "nohide"

    diretoriaExport = "\n"+diretoria+"/ "+ip_network+"("+optionOne+","+optionTwo+","+optionThree+")"
    f = open('/etc/exports', 'a')
    f.write(diretoriaExport)
    f.close()
    print("Directoria Adinionada com Sucesso!")


resposta_input = raw_input("Script do nfs, o que pretende fazer?\n1-Criar uma partilha\n2-Eliminar uma partilha\n3-Alterar uma Partilha\n")

if resposta_input =="1":
    dir = raw_input("Qual o nome da directoria que pretende criar e exportar?\n")
    if not os.path.exists(dir):
    		os.makedirs(dir)
    os.system("chown 65534.65534 "+dir.split())
    os.system("chmod 755 "+dir.split())
    exportsConfig(dir)

if resposta_input =="2":
    dir = raw_input("Qual o nome da directoria que pretende eliminar da partilha?\n")
    fin = open("teste.txt", "r")
    data = fin.readlines()
    fin.close()

    for i, line in enumerate(data):
            if dir in line:
                del data[i]

    fout =open("/etc/exports", "w")
    fout.writelines(data)
    fout.close()


if resposta_input =="3":
    dir = raw_input("Qual o nome da directoria que pretende alterar a partilha?\n")
    ip_network = raw_input("Qual o ip da network?(ex: 192.168.43.0/24)\n")
    optionsRead = raw_input("Options:\n1-Read and Write Acess.\n2-Read Only Acess.\n")
    
    if optionsRead =="1":
        optionOne = "rw"
    elif optionsRead =="2":
        optionOne = "ro"
 
    optionsWrites = raw_input("Options:\n1-Writes Data when the server feels the need, not the client.\n2-Writes data as it is received.\n")
    if optionsWrites =="1":
        optionTwo = "async"
    elif optionsWrites =="2":
        optionTwo = "sync"


    optionsHide = raw_input("Options:\n1-hide\n2-no hide\n")
    if optionsHide =="1":
        optionThree = "hide"
    elif optionsHide =="2":
        optionThree = "nohide"

    diretoriaExport = "\n"+dir+"/ "+ip_network+"("+optionOne+","+optionTwo+","+optionThree+")"
    fin = open("teste.txt", "r")
    data = fin.readlines()
    fin.close() 
    for i, line in enumerate(data):
            if dir in line:
                del data[i]
    fout = open("teste.txt", "w")
    fout.writelines(data)
    fout.close()
    f = open('teste.txt', 'a')
    f.write(diretoriaExport)
    f.close()
    print("Directoria Alterada com Sucesso!")

os.system("service nfs restart")