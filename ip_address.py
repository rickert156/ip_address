from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

ip_local = '' #Подставить  свой IP

def ipAddress():
	try:
		site = urlopen('https://api.ipify.org/')
		bs = BeautifulSoup(site, 'lxml')
		try:
			if bs.body.get_text() == ip_local:
				print(bs.body.get_text(),'Настоящий IP')
				# Сработает, если ip_local был указан заранее
			else:
				print(bs.body.get_text())
		except:
			print('Error')
	except:
		print("Error")
while True:
	ipAddress()
	time.sleep(1)
