import mod_driver
import mod_vpn
import cnf_bvb
from pyvirtualdisplay import Display
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# import requests
import requests , os
import io
from pydub import AudioSegment
import time , random
import emoji
import speech_recognition as sr


#https://ltc-earn.com/r/47CF451BF nx20y635a@adhoc-orange.com
#
#login_arry=['0cvyfgegg@adhoc-orange.com','keiyzs2ol@adhoc-white.com','nx20y635a@adhoc-orange.com']
# login_arry=['mooui@adhoc-red.com','lihgh6zyw@adhoc-red.com','lqompzwun@adhoc-white.com','isis@adhoc-red.com']
# login_email = random.choice(login_arry)
#old_amount="0"
#iroda8t1v@adhoc-yellow.com
balance_arry=[]
# fresh=['0cvyfgegg@adhoc-orange.com','keiyzs2ol@adhoc-white.com','nx20y635a@adhoc-orange.com','mooui@adhoc-red.com','lihgh6zyw@adhoc-red.com','lqompzwun@adhoc-white.com','isis@adhoc-red.com','k0h7qb61f@adhoc-purple.com','iroda8t1v@adhoc-yellow.com','jhxjyakc3@adhoc-green.com','lisipxnfk@adhoc-orange.com','8m34j47w0@adhoc-orange.com','4zzyoz60q@adhoc-yellow.com','ga9r9f8y1@adhoc-white.com','vnt8v13my@adhoc-red.com','9sr3j76ed@adhoc-green.com','i31lt5npk@adhoc-purple.com','3rrzdj2dl@adhoc-purple.com','qs8zt6fw0@adhoc-white.com','133gdzsbv@adhoc-orange.com','op4isulg8@adhoc-purple.com','tnb11a5e0@adhoc-green.com','p8z0f2ht0@adhoc-white.com','r5wzhv2gl@adhoc-yellow.com']
#
fresh=['1icdlc0kr@adhoc-yellow.com','ylabr3qv7@adhoc-purple.com','afztg11a8@adhoc-aqua.com','cuxduxhuc@adhoc-purple.com','icx8ao8f7@adhoc-white.com','urpyf7aui@adhoc-aqua.com','zutnjh7iw@adhoc-aqua.com','tvtfsgw70@adhoc-yellow.com','vjcx6ce8g@adhoc-purple.com','kkmx180sy@adhoc-aqua.com','j89pxhd8z@adhoc-yellow.com','sikhbkg6w@adhoc-red.com']
# fresh=['iroda8t1v@adhoc-yellow.com']
def ltc_login(login_email,width,height):

	try:
		# mod_vpn.fnc_vpn ()

		serv,ops=mod_driver.build_driver(width,height)
		driver = webdriver.Firefox(service=serv, options=ops)
		extension_path=cnf_bvb.extension_path
		extension_path_ublock=cnf_bvb.extension_path_ublock
		driver.install_addon(extension_path, True)
		driver.install_addon(extension_path_ublock, True)
		driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
		driver.get("https://ltc-earn.com/home")
		try:
			getLink_button=WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pageTop"]/nav/div/button/span/i')))
			time.sleep(2)
			getLink_button.click()

		except Exception as e:
			pass
		getLink_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '/html/body/header/nav/div/div/ul/li[5]')))
		time.sleep(2)
		getLink_button.click()
		time.sleep(2)
		getLink_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/form/div[1]/input')))
		getLink_button.click()
		time.sleep(1)
		getLink_button.send_keys(login_email)
		time.sleep(2)
		getLink_button.send_keys(Keys.TAB,"testpassword",Keys.ENTER)
		time.sleep(1)
		getLink_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="usd_balance"]')))	
		global old_amount
		old_amount=getLink_button.text
		print(old_amount)
		#balance_arry.append(old_amount)
		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		##################################################################""
		capatch(driver)
		# daily_offer(driver)
		#end_of_task(driver)
		pass
	except Exception as e:
		print(str(e))
		init_fire()


def daily_offer(driver):
	global bonnus_array
	bonnus_array=[]
	print("check daily offers")
	#//*[@id="navbarSupportedContent"]/ul/li[4]/a
	daily_button=WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.XPATH, '//*[@id="navbarSupportedContent"]/ul/li[4]/a')))	
	time.sleep(2)
	daily_button.click()
	time.sleep(3)
	number_links = driver.find_elements_by_tag_name("a")
	#print(str(number_links))
	for link in number_links:
		download_link = link.get_attribute('href')
		print(download_link)
		if "bonus/" in download_link:
			bonnus_array.append(download_link)
		else:
			pass
	print(bonnus_array)
	for ik in bonnus_array:
		print(ik)
		driver.get(ik)
		time.sleep(3)
		#/html/body/div/section/div/div[2]/div[3]/div/div[2]/div[3]/a
		visit_button=WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/section/div/div[2]/div[3]/div/div[2]/div[3]/a')))
		print('ok')
		visit_button.click()
		time.sleep(3)
		close_func(driver)
		time.sleep(2)


def audio_fonction(download_link):
	#data = open('1.mp3', 'rb').read()
	print("ok download_link")
	request = requests.get(download_link)
	audio_file = io.BytesIO(request.content)
	sound = AudioSegment.from_mp3(audio_file)
	dst = "test1.wav"
	sound.export(dst, format="wav")
	r = sr.Recognizer()
	with sr.WavFile("test1.wav") as source:
		audio = r.record(source)
	
	audio_output=r.recognize_google(audio)
	print("Transcription: " + audio_output)
	return audio_output


def close_func(driver):
	global new_amount
	driver_len = len(driver.window_handles) #fetching the Number of Opened tabs
	print("Length of Driver = ", driver_len)
	if driver_len > 1:
		for i in range(driver_len - 1, 0, -1):
			driver.switch_to.window(driver.window_handles[i])
			time.sleep(5)
			driver.close()
			print("Closed Tab No. ", i)
		driver.switch_to.window(driver.window_handles[0])
	else:
		print("Found only Single tab.")
	time.sleep(5)
	print('check balance ')
	getLink_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="usd_balance"]')))
	#global new_amount
	new_amount= getLink_button.text
	print(new_amount)

def capatch(driver):
	print("\n # STARTING CAPATCHA  ")
	print(" |")
	global new_amount
	#driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'without_captcha_button'))))
	without_captcha_button=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'without_captcha_button')))
	without_captcha_button.send_keys(Keys.TAB )
	time.sleep(2)
	main_button=WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'without_captcha_button')))
	time.sleep(5)
	number_fra=driver.find_elements_by_tag_name("iframe")
	print(str(len(number_fra)))#find_elements_by_class_name
	time.sleep(1)
	#input('check capatch')
	driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[2])
	time.sleep(2)
	recaptcha_ok=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="rc-anchor-container"]/div[3]/div[1]/div/div')))
	print(" |")
	recaptcha_ok.click()
	time.sleep(2)

	try:
		donne_ok=WebDriverWait(driver, 9).until(EC.presence_of_element_located((By.XPATH,'//span[@aria-checked="true"]')))
		print('lucky captcha')
		driver.switch_to.default_content()
		time.sleep(3)
		claim_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/div/div[2]/div[3]/form/div[4]/div[2]/a')))
		
		time.sleep(2)
		claim_button.click()
		print('lucky Cleaim')
		time.sleep(2)

		close_func(driver)
		end_of_task()
		#input('lucky captcha')
		# balance_arry.append(new_amount)	
	except Exception as e:
		print("no captch lucky")


	driver.switch_to.default_content()
	time.sleep(5)#input('lets go to audio')
	driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[8])
	recaptcha_ok=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'recaptcha-audio-button')))
	recaptcha_ok.click()
	time.sleep(3)
	eto_firstName=WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, 'audio-source')))
	download_link = eto_firstName.get_attribute('src')
	audio_output= audio_fonction(download_link)
	# input('OOOOOOOOO  go to audio')
	time.sleep(3)
	#main_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn.btn-main')))
	text_cap=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,'audio-response')))
	text_cap.send_keys(audio_output)
	time.sleep(2)
	text_cap.send_keys(Keys.ENTER)

	print('Captcha resolved')
	time.sleep(3)
	main_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.rc-audiochallenge-error-message')))
	#rc-audiochallenge-error-message
	captcha_error_message=main_button.text
	print(" 000 : "+captcha_error_message)
	if captcha_error_message.find("solve")!=-1:
		time.sleep(2)
		eto_firstName=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'audio-source')))
		download_link = eto_firstName.get_attribute('src')
		audio_output= audio_fonction(download_link)
		print('found error')
		text_cap=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,'audio-response')))
		text_cap.send_keys(audio_output)
		time.sleep(1)
		text_cap.send_keys(Keys.ENTER)


	else:
		print("Good Good")
	time.sleep(1)
	driver.switch_to.default_content()
	time.sleep(3)
	claim_button=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/div/div[2]/div[3]/form/div[4]/div[2]/a')))
	time.sleep(2)
	claim_button.click()
	time.sleep(2)
	close_func(driver)
	end_of_task()

def init_fire():
	print("############################################################")
	print("INIT TASKS ..... ", end='')
	try:
		os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#
		os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xephyr | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i geckodriver22 | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xvfb | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("rm -rf /tmp/*") 
		time.sleep(5)
		print(" OK !!!")
		#os.system("rm -rf __pycache__/")
		#print("############################################################")
	except  Exception as e :
		print(" NO  some_Error init_fire")
		print(str(e))

def end_of_task():
	try:
		print(" OK !!!"+old_amount+" -> "+new_amount)
		slack_message.append(old_amount+" -> "+new_amount)
	except Exception as e:
		print(str(e))
	init_fire()

def slack_fonction(s):
	cmdd="curl -X POST -H 'Content-type: application/json' --data "+"'"+'{"text":"'+s+'"}'+"'"+" https://hooks.slack.com/services/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"
	print (cmdd)
	os.system(cmdd)



################################-----------------------------

for i in fresh:
	init_fire()
	print(i)
	width , height =cnf_bvb.resolution_func()
	display = Display(visible=1, size=(width,height)).start()
	# slack_message.append(i)
	global slack_message
	slack_message=[]
	slack_message.append(i)
	ltc_login(i,width,height)
	s= ' # '.join(slack_message)
	slack_fonction(s)
	display.stop()
	os.system("rm -rf __pycache__/")
