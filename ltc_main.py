import cnf_bvb
import mod_vpn

import emoji
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random,datetime,string , os ,time ,subprocess , sys , requests ,re
from selenium.webdriver import ActionChains
import json

###########global urls_BVB
# urls_BVB=cnf_bvb.random_url
#####################################
urls_BVB="https://wild-beauty.weebly.com/about.html"

random_display_chose=cnf_bvb.random_display_chose
width=cnf_bvb.width
height=cnf_bvb.height

moz_wid="--width="+str(width)
moz_hig="--height="+str(height)

######################USER AGENT ###################################################
user_agent = cnf_bvb.user_agent
sys_use_agent=re.findall('\(.*?\)',user_agent)[0]

########################################################################################################################################
def build_driver():
	print("BUILDING PROFILE DRIVER  ...... ",end='')
	try:
		new_driver_path = cnf_bvb.new_driver_path
		new_binary_path = cnf_bvb.new_binary_path
		serv = Service(new_driver_path)
		fp = webdriver.FirefoxProfile()
		ops = Firefox_Options()
		#user_agent = cnf_bvb.user_agent
		#firefox_options = Firefox_Options()		
		ops.add_argument(moz_wid)
		ops.add_argument(moz_hig)
		
		fp.set_preference("dom.webdriver.enabled", False)
		fp.set_preference('useAutomationExtension', False)
		#fp.set_preference("http.response.timeout",95)
		fp.set_preference("general.useragent.override",user_agent)
		fp.set_preference('webdriver.load.strategy','unstable')
		fp.set_preference("modifyheaders.headers.count", 2)
		fp.set_preference("dom.webdriver.enabled", False)
		fp.set_preference("modifyheaders.headers.action0", "Add")
		fp.set_preference("modifyheaders.headers.name0", "x-msisdn")
		fp.set_preference("dom.push.enabled", False)
		fp.set_preference("intl.accept_languages", "en-GB");
		fp.update_preferences()
		ops.binary_location = new_binary_path
		ops.profile=fp
		#driver = webdriver.Firefox(service=serv, options=ops)
		#driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
		#driver.set_page_load_timeout(79)

		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
	except Exception as error:
		print("    Error !!!!! ----->"+str(error))
	return serv ,ops



def lets_play(serv,ops):

	try:
		print("OPEN DISPLAY  WEB-SITE ...... ",end='')
		display = Display(visible=0, size=(width,height)).start()
		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))


	except Exception as error:
		print(str(error))
		exit(0)
	
	print("OPEN AND VISITE WEB-SITE ...... ",end='')
	time.sleep(1)
	try:
		
		#print(ops)
		extension_path="/root/OUOIO/BVB/src/canvasblocker44b.xpi"
		driver = webdriver.Firefox(service=serv, options=ops)
		driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
		driver.set_page_load_timeout(79)
		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		driver.maximize_window()#
		driver.install_addon(extension_path, True)
		driver.get("https://inspiring-brattain-1201ff.netlify.app/")
		#input("")
		time.sleep(5)
		#print(driver.execute_script("return navigator.userAgent;"))
		driver.get(urls_BVB)
		time.sleep(5)

		
		###############


	except Exception as error:
		print(str(error))

	
	print("CHECK THE getLink_button WEB-SITE ...... ",end='')
	try:
		#######getLink
		getLink_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="368839048817395185"]')))
		time.sleep(5)
		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		
		action = ActionChains(driver)
		action.move_to_element(getLink_button).perform()
		#time.sleep(10)
		
		getLink_button.click()
		#input('oprn url')

		
		
		print(len(driver.window_handles))

		#input()
		time.sleep(22)
		driver_len = len(driver.window_handles) #fetching the Number of Opened tabs
		print("Length of Driver = ", driver_len)
		if driver_len > 1:
			for i in range(driver_len - 1, 0, -1):
				driver.switch_to.window(driver.window_handles[i])
				print(driver.current_url)
				time.sleep(7)

				driver.close()
				print("Closed Tab No. ", i)
			driver.switch_to.window(driver.window_handles[0])
		else:
			print("Found only Single tab.")
		#input()
		time.sleep(5)
	except Exception as error:
		print(str(error))









	try:
		print("Close Firefox ...... ",end='')
		driver.quit()

		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		time.sleep(1)
	except:
		pass
	try:
		print("Close Display ...... ",end='')
		display.stop()
		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
	except:
		pass


#####################################

def init_fire():
	print("############################################################")
	print("INIT TASKS ..... ", end='')
	try:
		os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#
		os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xephyr | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i geckodriver13 | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xvfb | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("rm -rf /tmp/*") 
		time.sleep(5)
		print(" OK !!!")
		#os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#print("############################################################")
	except:
		print(" NO  some_Error init_fire")
###################################################################################################


def stage_1():
	try:
		#print (urls_BVB)
		os.system("rm -rf /tmp/*") 
		os.system("clear && sleep 1") 
		print ( "-------------------------------------------------------")
		print(emoji.emojize("Website    : "+urls_BVB+' :check_mark_button: :alien:'))
		print(emoji.emojize("Resolution : "+random_display_chose+' :check_mark_button: :alien:'))
		#####TO DO PRINT ONLY THE SYSTEM
		#print(width+"x"+height)
		print("System     : "+sys_use_agent)
		print ( "-------------------------------------------------------")

	except Exception as error:
		print (str(error))




#################################"MAIN STARTING"##############################

def starting_tasks():
	try:
		stage_1()### CLEAR
		mod_vpn.fnc_vpn ()
		serv,ops=build_driver()
		#build_driver()###### BUILDING DRIVER
		lets_play(serv,ops)

	except Exception as error:
		print (str(error))
os.system("rm -rf /tmp/*") 
starting_tasks()
#starting_tasks()