from django.test import TestCase
from SBP_APP.views import MainPage
from SBP_APP.models import *
#from django.http import HttpRequest
#from django.template.loader import render_to_string

class Home_BAKSINADO_PageTest(TestCase):
	def test_SBP_mainpage_root_templateused(self):
		response=self.client.get('/')
		self.assertTemplateUsed(response,'mainpage.html')
	

	


	

	def test_only_saves_info_necessary(self):
		self.client.get('/')
		self.assertEqual(PersonalInfo.objects.count(),0)

	# def test_baksinado_displays_all_list_info(self):
	# 	PersonalInfo.objects.create(otc_fname='info_1')
	# 	PersonalInfo.objects.create(otc_fname='info_2')
	# 	response = self.client.get('/')
	# 	self.assertIn('info_1', response.content.decode())
	# 	self.assertIn('info_2',response.content.decode())

class  ORM_Test(TestCase):
	
	def test_baksinado_profile_saving_info(self):
		first_info = PersonalInfo()
		first_info.otc_fname ='Polo Jasty'
		first_info.otc_mname = 'Deguzman'
		first_info.otc_sname = 'Mabanag'
		first_info.otc_age = '21'
		first_info.otc_sex = 'Male'
		first_info.otc_status = 'Employed'
		first_info.otc_address = 'BLK18 LOT 15'
		first_info.otc_barangay = 'SAN ISIDRO II'
		first_info.otc_munincipality = 'DASMARINAS'
		first_info.otc_email = 'SBP@gmail.com'
		first_info.otc_contact_number = '0595126126'
		#first_info.otc_fname ='1: Polo Jasty Deguzman Mabanag 21 Male Employed BLK 15 LOT 11 MOLAVE STREET SAN ISIDRO II DASMARINAS CITY CAVITE SBP@gmail.com 0962327237'
		#first_info.otc_mname ='1: Deguzman'
		first_info.save()

		second_info = PersonalInfo()
		second_info.otc_fname = 'Trafalgar'
		second_info.otc_mname = 'D'
		second_info.otc_sname = 'Law'
		second_info.otc_age = '25'
		second_info.otc_sex = 'Male'
		second_info.otc_status = 'student'
		second_info.otc_address = 'BLK18 LOT 15'
		second_info.otc_barangay = 'SABAODY'
		second_info.otc_munincipality = 'DASMARINAS'
		second_info.otc_email = 'ONEPIECE@gmail.com'
		second_info.otc_contact_number = '0962326126'

		second_info.save()

		saved_info = PersonalInfo.objects.all()
		self.assertEqual(saved_info.count(),2)
		first_saved_info = saved_info[0]
		#first_saved_mname_info = saved_info[1]
		second_saved_info = saved_info[1]
		#second_saved_info = saved_info[1]
		self.assertEqual(first_saved_info.otc_fname,'Polo Jasty')
		#self.assertEqual(first_saved_info.otc_fname,'1: Polo Jasty Deguzman Mabanag 21 Male Employed BLK 15 LOT 11 MOLAVE STREET SAN ISIDRO II DASMARINAS CITY CAVITE SBP@gmail.com 0962327237')
		#self.assertEqual(first_saved_mname_info.otc_mname,'1: Deguzman ')
		self.assertEqual(second_saved_info.otc_fname,'Trafalgar')

class ListViewTest(TestCase):

	def test_uses_list_templates(self):
		response = self.client.get('/SBP_APP/BAKSINADO-LIST/')
		self.assertTemplateUsed(response,'sbplist.html')
	def test_baksinado_displays_all_list_info_view(self):
		PersonalInfo.objects.create(otc_fname='info_1')
		PersonalInfo.objects.create(otc_fname='info_2')
		response = self.client.get('/')
		self.assertContains(response,'info_1')
		self.assertContains(response,'info_2')

class NewListTest(TestCase):


	def test_baksinado_save_post_request(self):
		self.client.post('/SBP_APP/new',data ={
		'OTC_FIRSTNAME_ID':'OTC_FIRSTNAME_ID_VALUE',
		'OTC_MIDDLENAME_ID':'OTC_MIDDLENAME_ID_VALUE',
		'OTC_SURNAME_ID': 'OTC_SURNAME_ID_VALUE',
		'OTC_AGE_ID':'OTC_AGE_ID_VALUE',
		'OTC_SEX_ID':'OTC_SEX_ID_VALUE',
		'OTC_ESTATUS_ID':'OTC_ESTATUS_ID_VALUE',
		'OTC_ADDRESS_ID':'OTC_ADDRESS_ID_VALUE',
		'OTC_BARANGAY_ID':'OTC_BARANGAY_ID_VALUE',
		'OTC_MUNINCIPALITY_ID':'OTC_MUNINCIPALITY_ID_VALUE',
		'OTC_EMAIL_ID':'OTC_EMAIl_ID_VALUE',
		'OTC_CONTACTNUMBER_ID':'OTC_CONTACTNUMBER_ID_VALUE',
		})
		
		self.assertEqual(PersonalInfo.objects.count(),1)
		new_baksinado_info = PersonalInfo.objects.first()
		self.assertEqual(new_baksinado_info.text,'OTC_FIRSTNAME_ID_VALUE')
		

	def test_baksinado_redirects_after_POST(self):
		response =self.client.post('/SBP_APP/new',data ={
		'OTC_FIRSTNAME_ID':'OTC_FIRSTNAME_ID_VALUE'
		# 'OTC_MIDDLENAME_ID':'OTC_MIDDLENAME_ID_VALUE',
		# 'OTC_SURNAME_ID': 'OTC_SURNAME_ID_VALUE',
		# 'OTC_AGE_ID':'OTC_AGE_ID_VALUE',
		# 'OTC_SEX_ID':'OTC_SEX_ID_VALUE',
		# 'OTC_ESTATUS_ID':'OTC_ESTATUS_ID_VALUE',
		# 'OTC_ADDRESS_ID':'OTC_ADDRESS_ID_VALUE',
		# 'OTC_BARANGAY_ID':'OTC_BARANGAY_ID_VALUE',
		# 'OTC_MUNINCIPALITY_ID':'OTC_MUNINCIPALITY_ID_VALUE',
		# 'OTC_EMAIL_ID':'OTC_EMAIl_ID_VALUE',
		# 'OTC_CONTACTNUMBER_ID':'OTC_CONTACTNUMBER_ID_VALUE',
		})

		# self.assertEqual(response.status_code,302)
		self.assertRedirects(response,'/SBP_APP/BAKSINADO-LIST/')



























		#self.assertIn('OTC_AGE_ID_VALUE',response.content.decode())
		#self.assertIn('OTC_MIDDLENAME_ID_VALUE',response.content.decode())
		#self.assertIn('OTC_FIRSTNAME_ID_VALUE',response.content.decode())

		# self.assertTemplateUsed(response,'mainpage.html')
		# response =self.client.post('/',data ={
		# 'OTC_AGE_ID': 'OTC_AGE_ID_VALUE',
		# })
		# self.assertIn('OTC_AGE_ID_VALUE',response.content.decode())
		# self.assertTemplateUsed(response,'mainpage.html')

		# response =self.client.post('/',data ={
		# 'OTC_SEX_ID': 'OTC_SEX_ID_VALUE',
		# })
		# self.assertIn('OTC_SEX_ID_VALUE',response.content.decode())
		# self.assertTemplateUsed(response,'mainpage.html')

		# response =self.client.post('/',data ={
		# 'OTC_ESTATUS_ID': 'OTC_ESTATUS_ID_VALUE',
		# })
		# self.assertIn('OTC_ESTATUS_ID_VALUE',response.content.decode())
		# self.assertTemplateUsed(response,'mainpage.html')

		# response =self.client.post('/',data ={
		# 'OTC_ADDRESS_ID': 'OTC_ADDRESS_ID_VALUE',
		# })
		# self.assertIn('OTC_ADDRESS_ID_VALUE',response.content.decode())
		# self.assertTemplateUsed(response,'mainpage.html')

		# response =self.client.post('/',data ={
		# 'OTC_BARANGAY_ID': 'OTC_BARANGAY_ID_VALUE',
		# })
		# self.assertIn('OTC_BARANGAY_ID_VALUE',response.content.decode())
		# self.assertTemplateUsed(response,'mainpage.html')

		# response =self.client.post('/',data ={
		# 'OTC_MUNINCIPALITY_ID': 'OTC_MUNINCIPALITY_ID_VALUE',
		# })
		# self.assertIn('OTC_MUNINCIPALITY_ID_VALUE',response.content.decode())
		# self.assertTemplateUsed(response,'mainpage.html')

		# response =self.client.post('/',data ={
		# 'OTC_EMAIL_ID': 'OTC_EMAIL_ID_VALUE',
		# })
		# self.assertIn('OTC_EMAIL_ID_VALUE',response.content.decode())
		# self.assertTemplateUsed(response,'mainpage.html')

		# response =self.client.post('/',data ={
		# 'OTC_CONTACT_ID': 'OTC_CONTACT_ID_VALUE',
		# })
		# self.assertIn('OTC_CONTACT_ID_VALUE',response.content.decode())
		# self.assertTemplateUsed(response,'mainpage.html')
	"""
	def test_root_url_resolves_to_mainpage_view(self):
		found = resolve('/')
		self.assertEqual(found.func,MainPage)
		
	def test_mainpage_returns_correct_view(self):
		request = HttpRequest()
		response = MainPage(request)
		html = response.content.decode('utf8')
		#self.assertTrue(html.startswith('<html'))
		#self.assertIn('<title>OTC LIST</title>', html)
		#self.assertTrue(html.endswith('</html>'))
		string_html = render_to_string('mainpage.html')
		self.assertEqual(html,string_html)
		
	"""


