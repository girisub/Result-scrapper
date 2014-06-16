from selenium import webdriver
from selenium.webdriver.support.ui import Select

webpage = "http://www.nitt.edu/prm/nitreg/ShowRes.aspx"
driver = webdriver.Firefox()
driver.get(webpage)
for num in range (106112001,106112003):
	if(num!=106112088 and num!=106112044 and num!=106112058):
		box = driver.find_element_by_id("TextBox1")
		box.clear()
		box.send_keys(num)
		submit = driver.find_element_by_id("Button1")
		submit.click()
		select = Select(driver.find_element_by_id("Dt1"))
		select.select_by_value("96")
		name = driver.find_element_by_xpath("//span[@id='LblName']")
		print name.text
		roll = driver.find_element_by_xpath("//span[@id='LblEnrollmentNo']")
		print roll.text
		gpa = driver.find_element_by_xpath("//span[@id='LblGPA']")
		print gpa.text
		f = open("nitt.txt","a+")
		f.write(roll.text+'   ')
		f.write(gpa.text+'      ')
		f.write(name.text+'\n')