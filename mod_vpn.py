import os ,random ,subprocess,time 

import cnf_bvb


########################### VPN  #############################
file_vpn_dead=cnf_bvb.file_vpn_dead
p_vpn_dead=cnf_bvb.p_vpn_dead
##############################################################


def fnc_vpn():
	#final_vpn=cnf_bvb.final_vpn
	#print("openvpn "+final_vpn)
	#random_vpn=cnf_bvb.random_vpn
	final_vpn,random_vpn=cnf_bvb.randomm()
	print("###################################################")
	print("KILLING OPENVPN ....",end=' ')
	#random_vpn=random.choice(os.listdir(cnf_bvb.p_vpn_g))
	os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
	time.sleep(3)
	os.system("rm -rf /var/log/openvpn/openvpn.log")
	os.system("touch /var/log/openvpn/openvpn.log")
	print ("OK !!!!!")
	
	#print(final_vpn)
	print("STARTING VPN " , end="")
	x = subprocess.Popen(['openvpn', '--auth-nocache', '--config',final_vpn , '--log' , '/var/log/openvpn/openvpn.log'])
	time.sleep(15)
	print("["+random_vpn+"]" , end="")
	#c_ip,tz,loc=cnf_bvb.iip()
	with open ('/var/log/openvpn/openvpn.log', "r") as logfile:
		if logfile.read().find('Sequence Completed') !=-1:
			print ("OK !!!!!")
			ac_ip,tz,loc=cnf_bvb.iip()
			os.environ['TZ'] = tz
			print("VPN STATUS = OK || "+ random_vpn +"||"+ ac_ip+"||"+ tz)
			return [x ,True]
		else :
			print("")
			print("VPN STATUS = OFF || "+ random_vpn )
			# p_vpn_dead=cnf_bvb.p_vpn_dead
			# starting_tasks()
			# processs="mv ..{} ..{}".format(random_vpn,p_vpn_dead)
			# subprocess.run(processs ,shell=True)
			fnc_vpn ()
			return [x ,False]

	time.sleep(5)
	os.system("echo '' > /var/log/openvpn/openvpn.log")



	

########################################################################################################################################
def my_vpn ():
	init_fire()
	print("############################################################")
	print("KILLING OPENVPN ....",end=' ')
	random_vpn=random.choice(os.listdir(cnf_bvb.p_vpn_g))
	os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
	time.sleep(3)
	print ("OK !!!!!")
	os.system("rm -rf /var/log/openvpn/openvpn.log")
	c_ip,tz=iip()
	print(random_vpn)
	path = cnf_bvb.p_vpn_g+random_vpn
	print("STARTING VPN !!!" , end="")
	x = subprocess.Popen(['openvpn', '--auth-nocache', '--config',path , '--log' , '/var/log/openvpn/openvpn.log'])
	time.sleep(15)
	with open ('/var/log/openvpn/openvpn.log', "r") as logfile:
				
				if logfile.read().find('Sequence Completed') !=-1:
					print ("OK !!!!!")
					ac_ip,tz,loc=iip()
					os.environ['TZ'] = tz
					print("VPN STATUS = OK || "+ random_vpn +"||"+ ac_ip+"||"+ tz)
					#####--------------------------------------------###############################
					#starter()
					return [x ,True]
				else :
					print("VPN STATUS = OFF || "+ random_vpn )
					p_vpn_dead=cnf_bvb.p_vpn_dead
					starting_tasks()
					processs="mv ..{} ..{}".format(random_vpn,p_vpn_dead)
					subprocess.run(processs ,shell=True)
					return [x ,False]

					try:
						x.kill()
						#init_fire()
					except:
						pass

################################
def vpn1 ():
	try:
		#print(pwd)
		#print(final_vpn)
		processs="cp {} {}".format(final_vpn,p_vpn_dead)
		subprocess.run(processs ,shell=True)
	except Exception as e:
		raise e
#cnf_bvb.testt()
#fnc_vpn ()