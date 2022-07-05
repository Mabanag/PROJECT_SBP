from django.db import models

class PersonalInfo(models.Model):
	otc_firstname = models.CharField(max_length=200, null=True,blank=False)
	otc_middlename = models.CharField(max_length=200, null=True,blank=False)
	otc_lastname = models.CharField(max_length=200, null=True,blank=False)
	otc_age = models.CharField(max_length=200, null=True,blank=False)

	Sex_Choices  =(
		('Male','Male'),
		('Female','Female')
		)
	otc_sex = models.CharField(max_length=200, null=True,blank=True,choices=Sex_Choices)
	#otc_sex = models.CharField(max_length=200, null=True,blank=True)
	Status_Choices  =(
		('Student','Student'),
		('Employed','Employed'),
		('Nonemployed','Nonemployed')
		
		)
	#otc_status = models.CharField(max_length=200, null=True,blank=False)
	otc_status = models.CharField(max_length=200, null=True,blank=False, choices =Status_Choices)
	otc_address = models.CharField(max_length=200, null=True,blank=False)
	otc_barangay = models.CharField(max_length=200, null=True,blank=False)
	otc_munincipality = models.CharField(max_length=200, null=True,blank=False,)
	otc_email = models.EmailField(max_length=200, null=True,blank=False)
	otc_username = models.CharField(max_length=200, null=True,blank=False)
	otc_password = models.CharField(max_length=200, null=True,blank=False)
	otc_contact_number = models.CharField(max_length=200, null=True,blank=False)

	def __str__(self):
		return self.otc_firstname + ' ' + self.otc_middlename + ' ' + self.otc_lastname

class Vaccinations_Takein(models.Model):

	Personal_id_info = models.ForeignKey(PersonalInfo,null=True,on_delete= models.SET_NULL)
	
	Vac_Immunity_Choices =(
		('1st Dose','1st Dose'),
		('2nd Dose','2nd Dose'),
		('First Booster','First Booster'),
		('Second Booster','Second Booster'),
		)

	Vac_Immunity = models.CharField(max_length=200, null=True, choices=Vac_Immunity_Choices)

	Vaccination_Category_Choices= (
		('Pfizer','Pfizer'),
		('AstraZeneca','AstraZeneca'),
		('Sinovac','Sinovac'),
		('Sputnik','Sputnik'),
		('Johnsons Janssen','Johnsons Janssen'),
		('BioTech','BioTech'),
		('Moderna','Moderna'),
		)

	Vaccination_Category = models.CharField(max_length=200, null=True, choices= Vaccination_Category_Choices)

	Physical_Effects_Choices=(
		('Mild fever(Lagnat)','Mild fever(Lagnat)'),
		('Chills(Pagkalamig)','Chills(Pagkalamig)'),
		('Feeling tired(Pagod)','Feeling tired(Pagod)'),
		('Headache(Pagsakit ng ulo)','Headache(Pagsakit ng ulo)'),
		('Muscle and joint aches','Muscle and joint aches'),
		('None','None'),

		)
	
	#What are the physical body effects of the dose and type of vaccines that you receive?
	Physical_mild_Effects=models.CharField(max_length=500,null=True,blank=False,choices= Physical_Effects_Choices)

	Physical_Serious_Effects_Choices=(
		('Difficulty breathing(Hirap sa Paghinga)','Difficulty breathing(Hirap sa Paghinga'),
		('Swelling of your face(Pamamaga ng Muka)','Swelling of your face(Pagmamaga ng Muka'),
		('Swelling of your throat(Pamamaga ng Lalamunan)','Swelling of your throat(Pagmamaga ng Lalamunan'),
		('A fast heartbeat(palpitate)','A fast heartbeat(palpitate)'),
		('A bad rash all over your body(Pamamantal)','A bad rash all over your body(Pamamantal)'),
		('None','None'),

		)
	Physical_Serious_Effects=models.CharField(max_length=500,null=True,blank=False,choices= Physical_Serious_Effects_Choices)

	Mental_Effects_Choices=(
		('Depression','Depression'),
		('Anxiety','Anxiety'),
		('Locomotors Impairment(Pagkawalang balanse)','Locomotors Impairment(Pagkawalang balanse)'),
		('Sleep Deprivation(Hirap sa Pagtulog)','Sleep Deprivation(Hirap sa Pagtulog)'),
		('Loss of Memory and focus(Pagiging Malimutin)','Loss of Memory and focus(Pagiging Malimutin)'),
		('Hallucinations','Hallucinations'),
		('None','None'),

		)

	#What are the mentally effects of the dose and type of vaccines that you receive?
	Mental_Effects=models.CharField(max_length=1000,null=True, blank=False,choices= Mental_Effects_Choices)
	
	#Is it possible that the immunizations and doses you received triggered your previous illness?
	Trigger_Past_Illness=models.CharField(max_length=1000,null=True, blank=False)
	#What is your experience with doses and vaccines that have been injected into you?
	Experience_Effects=models.CharField(max_length=1000,null=True, blank =False)
	#date_created = models.DateTimeField(auto_now_add = True, null = True)
	date_created = models.CharField(max_length=1000,null=True, blank =False)





class Vaccinations_not_decide(models.Model):
	
	Personal_id_info = models.ForeignKey(PersonalInfo,null=True,on_delete= models.SET_NULL)

	Concern_Choices =(
		('I have concerns about the vaccines side effects,long-term safety and efficacy','I have concerns about the vaccines side effects,long-term safety and efficacy'),
		('I have religious reasons','I have religious reasons'),
		('I do not believe it will be a solution for coronavirus disease','I do not believe it will be a solution for coronavirus disease'),
		('I believe that it will have negative effects on my health','I believe that it will have negative effects on my health'),
		)

	#Which of the followings define your concerns about getting the vaccine?
	Concern_One= models.CharField(max_length=200, null=True,choices=Concern_Choices)

	#Which of the followings would be helpful if you did not decide yet?
	Concern_Two_Choices=(
		('If my doctor would approve','If my doctor would approve'),
		('If my family would approve','If my family would approve'),
		('I want to wait for a period to observe how other people react to the vaccine','I want to wait for a period to observe how other people react to the vaccine'),
		)
	Concern_Two = models.CharField(max_length=200, null=True,choices=Concern_Two_Choices)

	#What makes it difficult for you to get a COVID-19 vaccine?
	Concern_Three_Choices=(
		('I can’t go on my own.I have a physical limitation','I can’t go on my own.I have a physical limitation'),
		('I am too busy to get vaccinated','I am too busy to get vaccinated'),
		('I don’t know where to go to get vaccinated','I don’t know where to go to get vaccinated'),
		)

	Concern_Three = models.CharField(max_length=200, null=True,choices=Concern_Three_Choices)

	#We Gladly to know what are your other concerns?
	Other_Concern_Reason= models.TextField(max_length=1000, null=True,blank=True)


class Positive_effects(models.Model):

	Vac_effects_Choices =(
		('1st Dose','1st Dose'),
		('2nd Dose','2nd Dose'),
		('First Booster','First Booster'),
		('Second Booster','Second Booster'),
		)

	Vac_positive_Immunity = models.CharField(max_length=200, null=True, choices=Vac_effects_Choices)

	vaccination_types_positive_choices= (
		('Pfizer','Pfizer'),
		('AstraZeneca','AstraZeneca'),
		('Sinovac','Sinovac'),
		('Sputnik','Sputnik'),
		('Johnsons Janssen','Johnsons Janssen'),
		('BioTech','BioTech'),
		('Moderna','Moderna'),
		)

	Vaccination_Types_Category = models.CharField(max_length=200, null=True, choices= vaccination_types_positive_choices)

	vaccination_effects_felt_choices= (
		('Happy','Happy'),
		('Reliefs and Gratitude','Reliefs and Gratitude'),
		('freedom with care','freedom with care'),
		('Being Active','Being Active'),
		('None','None'),
		)

	Vaccination_Effects_Felt = models.CharField(max_length=200, null=True, choices= vaccination_effects_felt_choices)

	vaccination_effects_body_choices= (
		('Feeling energized','Feeling energized'),
		('Doing work lightly(mas magaan ang mga gawain)','Doing work lightly(mas magaan ang mga gawain)'),
		('Cherish little things about life','Cherish little things about life'),
		('No more sleeping deprivation ( hindi na hirap sa pagtulog)','No more sleeping deprivation ( hindi na hirap sa pagtulog)'),
		('None','None'),
		)

	Vaccination_Effects_Body_Felt = models.CharField(max_length=200, null=True, choices= vaccination_effects_body_choices)


	Positive_effects_one = models.CharField(max_length=200, null=True,blank=False)
	Positive_effects_two = models.CharField(max_length=200, null=True,blank=False)
	# Positive_effects_three = models.CharField(max_length=200, null=True,blank=False)
	date_created_vaccine = models.CharField(max_length=200, null=True,blank=False)


#SEVEN MODEL
# class Vaccine_effects_Concern_Messages(models.Model):
# 	Individuals = models.OnetoOneField(PersonalInfo)
# 	Concern_and_ =models.Textfield(default=" ")


#SEVEN MODEL
class Message_sbp(models.Model):
	Individuals = models.OneToOneField(PersonalInfo,null=True,on_delete= models.SET_NULL)
	Message_response =models.TextField(default=" ")