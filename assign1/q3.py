
import time
from datetime import datetime as dt

hostsPath="/etc/hosts"
redirect="127.0.0.1"

websites=["www.searchfusion.info"]
while True:
   
	if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,19):
		print ("Sorry Not Allowed...")
		with open(hostsPath,'r+') as file:
			content = file.read()
			for site in websites:
				if site in content:
					pass
				else:
					file.write(redirect+" "+site+"\n")
	else:
		with open(hostsPath,'r+') as file:
			content = file.readlines()
			file.seek(0)
			for line in content:
				if not any(site in line for site in websites):
					file.write(line)
			file.truncate()
		print ("Allowed access!")
	time.sleep(5)
