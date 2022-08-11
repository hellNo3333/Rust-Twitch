from cookie import cookies
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.chrome.options import Options   
from selenium import webdriver   
import time
import os
import math

anti_leak = True

options = Options()
options.add_argument("--mute-audio")
options.add_argument("--headless")

class API:
	def __init__(self, driver):
		self.TwitchPath = "https://twitch.tv/"
		self.Live = '//*[@id="live-channel-stream-information"]/div/div/div/div/div[1]/div/div/div/a/div[2]/div/div/div'
		self.isRust = '//*[@id="live-channel-stream-information"]/div/div/div/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div[1]/a/span'
		self.acceptMature = '//button[@data-a-target="player-overlay-mature-accept"]/div'
		self.claimNow = '//button[@data-test-selector="DropsCampaignInProgressRewardPresentation-claim-button"]/div/div[2]'
		self.Cookie = cookies
		self.driver = driver
		self.LoggingIn = False
		self.minutesToWatch = 190
		self.StreamerList = {}
		
		with open("streamers.txt", "r") as f:
			for line in f.readlines():
				stripped_line = line.strip()
				split_line = stripped_line.split(' ')
				self.StreamerList[split_line[0]] = float(split_line[1])
		
		self.game = "rust"

	def check_if_exists(self, xpath: str) -> bool:
		try:
			self.driver.find_element_by_xpath(xpath)
		except NoSuchElementException:
			return False
		return True

	def login(self) -> bool:
		for x in self.Cookie:
			self.driver.add_cookie(x)
		self.driver.refresh()
	
		return True
	
	def isLoggedin(self) -> bool:
		for x in self.driver.get_cookies():
			if x["value"].lower() == "hellno3333":  # this doesn't really seem to be doing anything, but whatever
				return True
		return False

	def gotoStreamer(self, streamer: str) -> bool:
		if anti_leak:
			self.driver.close()
			self.driver.quit()
			self.driver = webdriver.Chrome("driver" + os.path.sep + "chromedriver", options=options)
		self.driver.get(self.TwitchPath)
		for x in self.Cookie:
			self.driver.add_cookie(x)
		
		self.driver.execute_script("""localStorage["video-quality"] = '{"default": "160p30"}'; localStorage["mature"] = 'true';""")
		
		self.driver.get(self.TwitchPath + streamer)
		time.sleep(15)
		print(self.check_if_exists(self.Live))
		if self.check_if_exists(self.Live) and self.check_if_exists(self.isRust) and self.driver.find_element_by_xpath(self.isRust).text.lower() == self.game:
			return True
		return False


	def CreateTimer(self, streamer: str) -> bool:
		steps = math.ceil((-self.StreamerList[streamer] + self.minutesToWatch)/10)
		for x in range(steps):
			print("BA %d/%d" % (x, steps))
			if not self.gotoStreamer(streamer):
				self.LoggingIn = False
				return False
			
			if self.check_if_exists(self.acceptMature):
				self.driver.find_element_by_xpath(self.acceptMature).click()
				
			self.LoggingIn = True
			time.sleep(10 * 60)
			self.StreamerList[streamer] += 10
			
			with open("streamers.txt", "w") as f:
				for i in self.StreamerList:
					f.write(i + ' ' + str(self.StreamerList[i]) + '\n')
						
			if self.StreamerList[streamer] >= self.minutesToWatch:
				self.LoggingIn = False
				return True
		self.LoggingIn = False
		return True


	def BagItem(self):
		Bagged = False
		for x in self.Cookie:
			self.driver.add_cookie(x)
		self.driver.get("https://www.twitch.tv/drops/inventory")
		time.sleep(15)
		while True:
			if self.check_if_exists(self.claimNow):
				self.driver.find_element_by_xpath(self.claimNow).click()
				Bagged = True
			else:
				break
		return Bagged
	
	def isLogged(self) -> None:
		while True:
			if self.LoggingIn:
				if not self.isLoggedin():
					print("not logged")
					self.login()
			time.sleep(5)
