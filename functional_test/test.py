from selenium import webdriver
from django.test import LiveServerTestCase
import unittest
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

baksinado_antay = 6
class Baksinado_User_Test(LiveServerTestCase):
#class PageTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()


	def BAKSINADO_TABLE_LIST_CHECKING(self,row_text):
		simula =time.time()
		while time.time()-simula<baksinado_antay:
			time.sleep(0.5)
			try:
				table_vac = self.browser.find_element_by_id('VAC_LIST_TABLE')
				rows = table_vac.find_elements_by_tag_name('tr')
				self.assertIn(row_text,[row.text for row in rows])
				return
			except (AssertionError,Ay_may_error) as e:
			#except (AssertionError,WebDriverException) as e:

				if time.time()-simula>baksinado_antay :
					raise e
				time.sleep(1)

	def test_BAKSINADO_input_user_input(self):
		self.browser.get(self.live_server_url)
		#self.browser.get('http://localhost:8000')
		self.assertIn('SBP',self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('SAGUNIANG BAKSINADO PROTEKTADO',headerText)
		input_first_name_OTC = self.browser.find_element_by_id('OTC_FIRSTNAME_ID')
		input_middle_name_OTC = self.browser.find_element_by_id('OTC_MIDDLENAME_ID')
		input_surname_OTC = self.browser.find_element_by_id('OTC_SURNAME_ID')
		input_age_OTC = self.browser.find_element_by_id('OTC_AGE_ID')
		input_sex_OTC = self.browser.find_element_by_id('OTC_SEX_ID')
		input_estatus_OTC = self.browser.find_element_by_id('OTC_ESTATUS_ID')
		input_address_OTC = self.browser.find_element_by_id('OTC_ADDRESS_ID')
		input_barangay_OTC = self.browser.find_element_by_id('OTC_BARANGAY_ID')
		input_munincipality_OTC = self.browser.find_element_by_id('OTC_MUNINCIPALITY_ID')
		input_email_OTC = self.browser.find_element_by_id('OTC_EMAIL_ID')
		input_contactnumber_OTC = self.browser.find_element_by_id('OTC_CONTACTNUMBER_ID')
		BTN_FIRSTPAGE = self.browser.find_element_by_id('VAC_CONFIRM')
		self.assertEqual(input_first_name_OTC.get_attribute('placeholder'),'Enter your name here.')
		self.assertEqual(input_age_OTC.get_attribute('placeholder'),'Enter your Age.(ex.Student)')
		self.assertEqual(input_sex_OTC.get_attribute('placeholder'),'Enter your sex.(ex.Male)')
		self.assertEqual(input_estatus_OTC.get_attribute('placeholder'),'Enter your status.(ex.Student)')
		self.assertEqual(input_address_OTC.get_attribute('placeholder'),'Enter your address.(ex.Bldg 18)')
		self.assertEqual(input_barangay_OTC.get_attribute('placeholder'),'Enter your barangay (ex. Madrigal 2nd)')
		self.assertEqual(input_munincipality_OTC.get_attribute('placeholder'),'Enter your munincipality (ex. Dasmarinas Cavite City)')
		self.assertEqual(input_email_OTC.get_attribute('placeholder'),'Enter your email (ex. SBP@gmail.com)')
		self.assertEqual(input_contactnumber_OTC.get_attribute('placeholder'),'Enter your contactnumber (ex. 09512723728)')
		
	
		input_first_name_OTC.click()
		input_first_name_OTC.send_keys('Trafalgar')
		time.sleep(0.5)
		#input_first_name_OTC.send_keys(Keys.ENTER)

		input_middle_name_OTC.click()
		time.sleep(0.5)
		input_middle_name_OTC.send_keys('D')
		#input_middle_name_OTC.send_keys(Keys.ENTER)

		input_surname_OTC.click()
		time.sleep(0.5)
		input_surname_OTC.send_keys('Law')
	
		#input_surname_OTC.send_keys(Keys.ENTER)
		
		
		input_age_OTC.click()	
		input_age_OTC.send_keys('24')
		#input_age_OTC.send_keys(Keys.ENTER)
		time.sleep(0.5)
		

		input_sex_OTC.click()	
		input_sex_OTC.send_keys('MALE')
		#input_age_OTC.send_keys(Keys.ENTER)
		time.sleep(0.5)

		input_estatus_OTC.click()	
		time.sleep(0.5)
		input_estatus_OTC.send_keys('STUDENT')
		#input_age_OTC.send_keys(Keys.ENTER)
		


		input_address_OTC.click()
		time.sleep(0.5)	
		input_address_OTC.send_keys('BLK 15 LOT 11 MOLAVE STREET')
		#input_age_OTC.send_keys(Keys.ENTER)
		

		input_barangay_OTC.click()
		time.sleep(0.5)	
		input_barangay_OTC.send_keys('SABAODY ')
		#input_age_OTC.send_keys(Keys.ENTER)

		input_munincipality_OTC.click()
		time.sleep(0.5)	
		input_munincipality_OTC.send_keys('DASMARINAS CITY CAVITE ')
		#input_age_OTC.send_keys(Keys.ENTER)
		

		input_email_OTC.click()
		time.sleep(0.5)	
		input_email_OTC.send_keys('ONEPIECE@gmail.com')
		#input_age_OTC.send_keys(Keys.ENTER)


		input_contactnumber_OTC.click()
		time.sleep(0.5)	
		input_contactnumber_OTC.send_keys('0962327237')
		#input_age_OTC.send_keys(Keys.ENTER)

		time.sleep(1)

		BTN_FIRSTPAGE.click()
		



		input_first_name_OTC = self.browser.find_element_by_id('OTC_FIRSTNAME_ID')
		input_middle_name_OTC = self.browser.find_element_by_id('OTC_MIDDLENAME_ID')
		input_surname_OTC = self.browser.find_element_by_id('OTC_SURNAME_ID')
		input_age_OTC = self.browser.find_element_by_id('OTC_AGE_ID')
		input_sex_OTC = self.browser.find_element_by_id('OTC_SEX_ID')
		input_estatus_OTC = self.browser.find_element_by_id('OTC_ESTATUS_ID')
		input_address_OTC = self.browser.find_element_by_id('OTC_ADDRESS_ID')
		input_barangay_OTC = self.browser.find_element_by_id('OTC_BARANGAY_ID')
		input_munincipality_OTC = self.browser.find_element_by_id('OTC_MUNINCIPALITY_ID')
		input_email_OTC = self.browser.find_element_by_id('OTC_EMAIL_ID')
		input_contactnumber_OTC = self.browser.find_element_by_id('OTC_CONTACTNUMBER_ID')
		BTN_FIRSTPAGE = self.browser.find_element_by_id('VAC_CONFIRM')
		self.assertEqual(input_first_name_OTC.get_attribute('placeholder'),'Enter your name here.')
		self.assertEqual(input_age_OTC.get_attribute('placeholder'),'Enter your Age.(ex.Student)')
		self.assertEqual(input_sex_OTC.get_attribute('placeholder'),'Enter your sex.(ex.Male)')
		self.assertEqual(input_estatus_OTC.get_attribute('placeholder'),'Enter your status.(ex.Student)')
		self.assertEqual(input_address_OTC.get_attribute('placeholder'),'Enter your address.(ex.Bldg 18)')
		self.assertEqual(input_barangay_OTC.get_attribute('placeholder'),'Enter your barangay (ex. Madrigal 2nd)')
		self.assertEqual(input_munincipality_OTC.get_attribute('placeholder'),'Enter your munincipality (ex. Dasmarinas Cavite City)')
		self.assertEqual(input_email_OTC.get_attribute('placeholder'),'Enter your email (ex. SBP@gmail.com)')
		self.assertEqual(input_contactnumber_OTC.get_attribute('placeholder'),'Enter your contactnumber (ex. 09512723728)')
		#self.assertEqual(input_middle_name_OTC.get_attribute('placeholder'),'Enter your name here.')
		#self.assertEqual(input_first_name_OTC.get_attribute('placeholder'),'Enter your name here.')

		#self.assertEqual(input_age_OTC.get_attribute('placeholder'),'IYONG EDAD')	
		
	
		input_first_name_OTC.click()
		input_first_name_OTC.send_keys('Polo Jasty')
		time.sleep(0.5)
		#input_first_name_OTC.send_keys(Keys.ENTER)

		input_middle_name_OTC.click()
		time.sleep(0.5)
		input_middle_name_OTC.send_keys('Deguzman')
		#input_middle_name_OTC.send_keys(Keys.ENTER)

		input_surname_OTC.click()
		time.sleep(1)
		input_surname_OTC.send_keys('Mabanag')
	
		#input_surname_OTC.send_keys(Keys.ENTER)
		
		
		input_age_OTC.click()	
		input_age_OTC.send_keys('21')
		#input_age_OTC.send_keys(Keys.ENTER)
		time.sleep(0.5)
		

		input_sex_OTC.click()
		input_sex_OTC.send_keys('MALE')
		#input_age_OTC.send_keys(Keys.ENTER)
		time.sleep(0.5)

		input_estatus_OTC.click()	
		#time.sleep(0.5)
		input_estatus_OTC.send_keys('EMPLOYED')
		#input_age_OTC.send_keys(Keys.ENTER)
		


		input_address_OTC.click()
		time.sleep(0.5)	
		input_address_OTC.send_keys('BLK 15 LOT 11 MOLAVE STREET')
		#input_age_OTC.send_keys(Keys.ENTER)
		

		input_barangay_OTC.click()
		time.sleep(0.5)	
		input_barangay_OTC.send_keys('SAN ISIDRO II')
		#input_age_OTC.send_keys(Keys.ENTER)

		input_munincipality_OTC.click()
		time.sleep(0.5)	
		input_munincipality_OTC.send_keys('DASMARINAS CITY CAVITE ')
		#input_age_OTC.send_keys(Keys.ENTER)
		

		input_email_OTC.click()
		time.sleep(0.5)	
		input_email_OTC.send_keys('SBP@gmail.com')
		#input_age_OTC.send_keys(Keys.ENTER)


		input_contactnumber_OTC.click()
		time.sleep(0.5)	
		input_contactnumber_OTC.send_keys('0962327237')
		#input_age_OTC.send_keys(Keys.ENTER)

		time.sleep(1)

		BTN_FIRSTPAGE.click()
		#self.BAKSINADO_TABLE_LIST_CHECKING('1: Polo Jasty Deguzman Mabanag 21')
		
		

		#self.BAKSINADO_TABLE_LIST_CHECKING('1: Polo Jasty D Mabanag 21 Male Employed BLK 15 LOT 11 MOLAVE STREET SAN ISIDRO II DASMARINAS CITY CAVITE SBP@gmail.com 0962327237')
		self.BAKSINADO_TABLE_LIST_CHECKING('1: Trafalgar D Law 24 MALE STUDENT BLK 15 LOT 11 MOLAVE STREET SABAODY DASMARINAS CITY CAVITE ONEPIECE@gmail.com 0962327237')
		self.BAKSINADO_TABLE_LIST_CHECKING('2: Polo Jasty Deguzman Mabanag 21 MALE EMPLOYED BLK 15 LOT 11 MOLAVE STREET SAN ISIDRO II DASMARINAS CITY CAVITE SBP@gmail.com 0962327237')
		#self.BAKSINADO_TABLE_LIST_CHECKING('1: Trafalgar D Law 21')
		#self.BAKSINADO_TABLE_LIST_CHECKING('2: Polo Jasty')


		

	def test_BAKSINADO_another_user_input(self):
		self.browser.get(self.live_server_url)
		#self.browser.get('http://localhost:8000')
		self.assertIn('SBP',self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('SAGUNIANG BAKSINADO PROTEKTADO',headerText)
		input_first_name_OTC = self.browser.find_element_by_id('OTC_FIRSTNAME_ID')
		input_middle_name_OTC = self.browser.find_element_by_id('OTC_MIDDLENAME_ID')
		input_surname_OTC = self.browser.find_element_by_id('OTC_SURNAME_ID')
		input_age_OTC = self.browser.find_element_by_id('OTC_AGE_ID')
		input_sex_OTC = self.browser.find_element_by_id('OTC_SEX_ID')
		input_estatus_OTC = self.browser.find_element_by_id('OTC_ESTATUS_ID')
		input_address_OTC = self.browser.find_element_by_id('OTC_ADDRESS_ID')
		input_barangay_OTC = self.browser.find_element_by_id('OTC_BARANGAY_ID')
		input_munincipality_OTC = self.browser.find_element_by_id('OTC_MUNINCIPALITY_ID')
		input_email_OTC = self.browser.find_element_by_id('OTC_EMAIL_ID')
		input_contactnumber_OTC = self.browser.find_element_by_id('OTC_CONTACTNUMBER_ID')
		BTN_FIRSTPAGE = self.browser.find_element_by_id('VAC_CONFIRM')
		self.assertEqual(input_first_name_OTC.get_attribute('placeholder'),'Enter your name here.')
		self.assertEqual(input_age_OTC.get_attribute('placeholder'),'Enter your Age.(ex.Student)')
		self.assertEqual(input_sex_OTC.get_attribute('placeholder'),'Enter your sex.(ex.Male)')
		self.assertEqual(input_estatus_OTC.get_attribute('placeholder'),'Enter your status.(ex.Student)')
		self.assertEqual(input_address_OTC.get_attribute('placeholder'),'Enter your address.(ex.Bldg 18)')
		self.assertEqual(input_barangay_OTC.get_attribute('placeholder'),'Enter your barangay (ex. Madrigal 2nd)')
		self.assertEqual(input_munincipality_OTC.get_attribute('placeholder'),'Enter your munincipality (ex. Dasmarinas Cavite City)')
		self.assertEqual(input_email_OTC.get_attribute('placeholder'),'Enter your email (ex. SBP@gmail.com)')
		self.assertEqual(input_contactnumber_OTC.get_attribute('placeholder'),'Enter your contactnumber (ex. 09512723728)')
		#self.assertEqual(input_middle_name_OTC.get_attribute('placeholder'),'Enter your name here.')
		#self.assertEqual(input_first_name_OTC.get_attribute('placeholder'),'Enter your name here.')

		#self.assertEqual(input_age_OTC.get_attribute('placeholder'),'IYONG EDAD')	
		
	
		input_first_name_OTC.click()
		input_first_name_OTC.send_keys('Polo Jasty')
		time.sleep(0.5)
		#input_first_name_OTC.send_keys(Keys.ENTER)

		input_middle_name_OTC.click()
		time.sleep(0.5)
		input_middle_name_OTC.send_keys('Deguzman')
		#input_middle_name_OTC.send_keys(Keys.ENTER)

		input_surname_OTC.click()
		time.sleep(1)
		input_surname_OTC.send_keys('Mabanag')
	
		#input_surname_OTC.send_keys(Keys.ENTER)
		
		
		input_age_OTC.click()	
		input_age_OTC.send_keys('21')
		#input_age_OTC.send_keys(Keys.ENTER)
		time.sleep(0.5)
		

		input_sex_OTC.click()
		input_sex_OTC.send_keys('MALE')
		#input_age_OTC.send_keys(Keys.ENTER)
		time.sleep(0.5)

		input_estatus_OTC.click()	
		time.sleep(0.5)
		input_estatus_OTC.send_keys('EMPLOYED')
		#input_age_OTC.send_keys(Keys.ENTER)
		


		input_address_OTC.click()
		time.sleep(0.5)	
		input_address_OTC.send_keys('BLK 15 LOT 11 MOLAVE STREET')
		#input_age_OTC.send_keys(Keys.ENTER)
		

		input_barangay_OTC.click()
		time.sleep(0.5)	
		input_barangay_OTC.send_keys('SAN ISIDRO II')
		#input_age_OTC.send_keys(Keys.ENTER)

		input_munincipality_OTC.click()
		time.sleep(0.5)	
		input_munincipality_OTC.send_keys('DASMARINAS CITY CAVITE ')
		#input_age_OTC.send_keys(Keys.ENTER)
		

		input_email_OTC.click()
		time.sleep(0.5)	
		input_email_OTC.send_keys('SBP@gmail.com')
		#input_age_OTC.send_keys(Keys.ENTER)


		input_contactnumber_OTC.click()
		time.sleep(0.5)	
		input_contactnumber_OTC.send_keys('0962327237')
		#input_age_OTC.send_keys(Keys.ENTER)

		time.sleep(1)

		BTN_FIRSTPAGE.click()
		#self.BAKSINADO_TABLE_LIST_CHECKING('1: Polo Jasty Deguzman Mabanag 21')
		self.BAKSINADO_TABLE_LIST_CHECKING('1: Polo Jasty Deguzman Mabanag 21 MALE EMPLOYED BLK 15 LOT 11 MOLAVE STREET SAN ISIDRO II DASMARINAS CITY CAVITE SBP@gmail.com 0962327237')
		#self.BAKSINADO_TABLE_LIST_CHECKING('1:Polo Jasty')

		polo_list_url = self.browser.current_url
		self.assertRegex(polo_list_url,'/SBP_APP/.+')



		self.browser.quit()
		self.browser = webdriver.Firefox()

		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertNotIn('1: Trafalgar D Law 24 MALE STUDENT BLK 15 LOT 11 MOLAVE STREET SABAODY DASMARINAS CITY CAVITE ONEPIECE@gmail.com 0962327237',headerText)
		self.assertNotIn('2: Polo Jasty Deguzman Mabanag 21 MALE EMPLOYED BLK 15 LOT 11 MOLAVE STREET SAN ISIDRO II DASMARINAS CITY CAVITE SBP@gmail.com 0962327237',headerText)


		input_first_name_OTC = self.browser.find_element_by_id('OTC_FIRSTNAME_ID')
		input_middle_name_OTC = self.browser.find_element_by_id('OTC_MIDDLENAME_ID')
		input_surname_OTC = self.browser.find_element_by_id('OTC_SURNAME_ID')
		input_age_OTC = self.browser.find_element_by_id('OTC_AGE_ID')
		input_sex_OTC = self.browser.find_element_by_id('OTC_SEX_ID')
		input_estatus_OTC = self.browser.find_element_by_id('OTC_ESTATUS_ID')
		input_address_OTC = self.browser.find_element_by_id('OTC_ADDRESS_ID')
		input_barangay_OTC = self.browser.find_element_by_id('OTC_BARANGAY_ID')
		input_munincipality_OTC = self.browser.find_element_by_id('OTC_MUNINCIPALITY_ID')
		input_email_OTC = self.browser.find_element_by_id('OTC_EMAIL_ID')
		input_contactnumber_OTC = self.browser.find_element_by_id('OTC_CONTACTNUMBER_ID')
		BTN_FIRSTPAGE = self.browser.find_element_by_id('VAC_CONFIRM')
		self.assertEqual(input_first_name_OTC.get_attribute('placeholder'),'Enter your name here.')
		self.assertEqual(input_age_OTC.get_attribute('placeholder'),'Enter your Age.(ex.Student)')
		self.assertEqual(input_sex_OTC.get_attribute('placeholder'),'Enter your sex.(ex.Male)')
		self.assertEqual(input_estatus_OTC.get_attribute('placeholder'),'Enter your status.(ex.Student)')
		self.assertEqual(input_address_OTC.get_attribute('placeholder'),'Enter your address.(ex.Bldg 18)')
		self.assertEqual(input_barangay_OTC.get_attribute('placeholder'),'Enter your barangay (ex. Madrigal 2nd)')
		self.assertEqual(input_munincipality_OTC.get_attribute('placeholder'),'Enter your munincipality (ex. Dasmarinas Cavite City)')
		self.assertEqual(input_email_OTC.get_attribute('placeholder'),'Enter your email (ex. SBP@gmail.com)')
		self.assertEqual(input_contactnumber_OTC.get_attribute('placeholder'),'Enter your contactnumber (ex. 09512723728)')


		input_first_name_OTC.click()
		input_first_name_OTC.send_keys('Eutass')
		time.sleep(0.5)
		#input_first_name_OTC.send_keys(Keys.ENTER)

		input_middle_name_OTC.click()
		time.sleep(0.5)
		input_middle_name_OTC.send_keys('D')
		#input_middle_name_OTC.send_keys(Keys.ENTER)

		input_surname_OTC.click()
		time.sleep(1)
		input_surname_OTC.send_keys('Kid')
	
		#input_surname_OTC.send_keys(Keys.ENTER)
		
		
		input_age_OTC.click()	
		input_age_OTC.send_keys('21')
		#input_age_OTC.send_keys(Keys.ENTER)
		time.sleep(0.5)
		

		input_sex_OTC.click()
		input_sex_OTC.send_keys('MALE')
		#input_age_OTC.send_keys(Keys.ENTER)
		time.sleep(0.5)

		input_estatus_OTC.click()	
		time.sleep(0.5)
		input_estatus_OTC.send_keys('EMPLOYED')
		#input_age_OTC.send_keys(Keys.ENTER)
		


		input_address_OTC.click()
		time.sleep(0.5)	
		input_address_OTC.send_keys('BLK 15 LOT 11 MOLAVE STREET')
		#input_age_OTC.send_keys(Keys.ENTER)
		

		input_barangay_OTC.click()
		time.sleep(0.5)	
		input_barangay_OTC.send_keys('SAN ISIDRO II')
		#input_age_OTC.send_keys(Keys.ENTER)

		input_munincipality_OTC.click()
		time.sleep(0.5)	
		input_munincipality_OTC.send_keys('DASMARINAS CITY CAVITE ')
		#input_age_OTC.send_keys(Keys.ENTER)
		

		input_email_OTC.click()
		time.sleep(0.5)	
		input_email_OTC.send_keys('SBP@gmail.com')
		#input_age_OTC.send_keys(Keys.ENTER)


		input_contactnumber_OTC.click()
		time.sleep(0.5)	
		input_contactnumber_OTC.send_keys('0962327237')
		#input_age_OTC.send_keys(Keys.ENTER)

		time.sleep(1)

		BTN_FIRSTPAGE.click()
		self.BAKSINADO_TABLE_LIST_CHECKING('1: Eutass D Kid 21 MALE EMPLOYED BLK 15 LOT 11 MOLAVE STREET SAN ISIDRO II DASMARINAS CITY CAVITE SBP@gmail.com 0962327237')

		eutass_list_url = self.browser.current_url
		self.assertRegex(eutass_list_url,'/SBP_APP/.+')
		self.assertNotEqual(eutass_list_url, eutass_list_url)


		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertNotIn('1: Polo Jasty Deguzman Mabanag 21 MALE EMPLOYED BLK 15 LOT 11 MOLAVE STREET SAN ISIDRO II DASMARINAS CITY CAVITE SBP@gmail.com 0962327237')
		self.assertIn('1: Eutass D Kid 21 MALE EMPLOYED BLK 15 LOT 11 MOLAVE STREET SAN ISIDRO II DASMARINAS CITY CAVITE SBP@gmail.com 0962327237',headerText)