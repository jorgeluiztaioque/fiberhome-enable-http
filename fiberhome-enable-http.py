#!/usr/bin/env python
# Jorge Luiz Taioque
# jorgeluiztaioque at gmail dot com 
#
# Executando:
# ./fiberhome-allow-web.py
#
#


import sys,pexpect
import getpass
import time
import sys


#Comando padrao
#set onu_local_manage_config slot 01 link 16 onu 9 config_enable_switch enable console_switch enable telnet_switch enable web_switch enable web_port 8080 web_ani_switch enable tel_ani_switch enable

'''
CONFIGURACOES DE LOGIN DA OLT (PADRÃO) E PORTA HTTP
'''
USER = 'GEPON'
PASSWORD = 'GEPON'
ENPASSWORD = 'GEPON'
HTTPDEFAULT = '80'

def set_config(HOST,slot,pon,onu,httpport):
	if httpport == "":
		httpport = HTTPDEFAULT
	print ('===========================================')
	print (' Configurando a ONU com os parametros: ')
	print('OLT = '+HOST)
	print('OLT SLOT = '+slot)
	print("PONTA PON = "+pon)
	print('ONU ID = '+onu)
	print('PORTA HTTP = '+httpport)

	child = pexpect.spawn ('telnet '+HOST) #option needs to be a list
	#child.timeout = 150
	#child.logfile = sys.stdout #display progress on screen
	time.sleep(2)

	child.expect ('Login:')
	child.sendline (USER)

	child.expect('Password:')
	child.sendline (PASSWORD)
	time.sleep(1)

	child.sendline ('enable')
	time.sleep(1)

	child.expect('Password:')
	time.sleep(1)
	child.sendline (ENPASSWORD)

	time.sleep(1)
	child.expect('Admin# ')
	time.sleep(1)
	child.sendline ('cd gponon \r')
	time.sleep(1)
	child.expect('gpononu# ')
	time.sleep(1)
	child.sendline ('set onu_local_manage_config slot '+slot+' link '+pon+' onu '+onu+' config_enable_switch enable console_switch enable telnet_switch enable web_switch enable web_port '+httpport+' web_ani_switch enable tel_ani_switch enable \r')
	time.sleep(1)
	child.expect('gpononu# ')
	time.sleep(1)
	child.sendline ('cd .. \r')
	time.sleep(1)
	child.expect('Admin# ')
	time.sleep(1)
	child.sendline ('exit \r')
	time.sleep(1)
	child.expect('>')
	child.sendline ('exit \r')
	print ('-------------------------------------------')
	print ('Configuracao da ONU finalizada com sucesso..')
	return 0

def menu():
	print ('-------------------------------------------')
	print (' Fiberhome - Habilitar gerencia web na ONU ')
	print ('-------------------------------------------')
	HOST = raw_input("IP da olt: ") 
	slot = raw_input("Numero do slot da placa PON: ") 
	pon = raw_input("Numero da porta PON: ") 
	onu = raw_input("ID da ONU: ") 
	httpport = raw_input('Porta http (padrao porta '+HTTPDEFAULT+'): ')
	set_config(HOST,slot,pon,onu,httpport)
	return 0

menu()
