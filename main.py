from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from API import API
import sys
import os

options = Options()
options.add_argument("--headless")
options.add_argument("--mute-audio")

def main():
	res = False
	driver = webdriver.Chrome("driver" + os.path.sep + "chromedriver", options=options)
	Api = API(driver)
	driver.get("https://www.twitch.tv/")

	x = True

	try:
		while x:
			for x in Api.StreamerList:
				if Api.StreamerList[x] < Api.minutesToWatch:
					if Api.CreateTimer(x):
						if Api.BagItem():
							print("Bagged {} item".format(x))
						else:
							print("Missed item")

			time.sleep(2)

	except Exception as e:
		print(e)
		with open(str(time.time()) + ".txt", 'w') as f:
			f.write(str(e))
		if not res:
			res = True
			driver.close()
			driver.quit()
			main()

main()
