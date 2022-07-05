from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from django.core.paginator import Paginator


def Mainpage(request):
	return render(request,'Mainpage.html')


def Protektayo_Personal_Info(request):
	if request.method == "POST":
		otc_email = request.POST['otc_email']
		otc_password = request.POST['otc_password']
		otc_firstname = request.POST['otc_firstname']
		otc_middlename = request.POST['otc_middlename']
		otc_lastname = request.POST['otc_lastname']
		otc_age = request.POST['otc_age']
		otc_sex = request.POST['otc_sex']
		otc_status = request.POST['otc_status']
		otc_address = request.POST['otc_address']
		otc_barangay = request.POST['otc_barangay']
		otc_munincipality = request.POST['otc_munincipality']
		otc_contact_number = request.POST['otc_contact_number']
		personal_info = PersonalInfo(
		otc_email = otc_email,
		otc_password = otc_password,
		otc_firstname = otc_firstname,
		otc_middlename = otc_middlename,
		otc_lastname = otc_lastname,
		otc_age = otc_age,
		otc_sex = otc_sex,
		otc_status = otc_status,
		otc_address = otc_address,
		otc_barangay = otc_barangay,
		otc_munincipality = otc_munincipality,
		
		otc_contact_number = otc_contact_number,
		)
		personal_info.save()
		#return redirect('/')
		#messages.info(request,"SBP Member Registration Successful")
		messages.success(request,'SBP Member Registration Succesful '+request.POST['otc_email'])


	else:
		return render(request,'protektado_tayo_info_two.html')

	otc_members = PersonalInfo.objects.all()

	return render(request,'protektado_tayo_info_two.html',{'otc_members':otc_members})


def Delete_sbp_member(request,sbpid):
	personal_info =PersonalInfo.objects.get(id = sbpid)
	personal_info.delete()
	#message.info(request,"SBP MEMBER DELETED")
	#return redirect('')

	return render(request,'SBP_deleted.html')


def Edit_sbp_member(request,sbpid):
	sbp_edit_info =PersonalInfo.objects.get(id = sbpid)
	otc_members = PersonalInfo.objects.all()
	return render(request,'protektado_tayo_info_two.html',{'sbp_edit_info':sbp_edit_info,
		'otc_members':otc_members,
		})


def Update_sbp_member(request,sbpid):
	otc_members = PersonalInfo.objects.get(id = sbpid)
	otc_members.otc_firstname = request.POST['otc_firstname']
	otc_members.otc_middlename = request.POST['otc_middlename']
	otc_members.otc_lastname = request.POST['otc_lastname']
	otc_members.otc_age = request.POST['otc_age']
	otc_members.otc_sex = request.POST['otc_sex']
	otc_members.otc_status = request.POST['otc_status']
	otc_members.otc_barangay = request.POST['otc_barangay']
	otc_members.otc_munincipality = request.POST['otc_munincipality']
	otc_members.otc_email = request.POST['otc_email']
	otc_members.otc_contact_number = request.POST['otc_contact_number']
	otc_members.save()
	#messages.info(request,"SBP Member Succesful Update")
	return redirect('Vaccine_effect_updated')



def Login_sbp(request):
	if request.method == "POST":
		try:
			SBT_login=PersonalInfo.objects.get(otc_email=request.POST['otc_email'],otc_password=request.POST['otc_password'])
			print("otc_email",SBT_login)
			request.session['otc_email']=SBT_login.otc_email
			return render(request,'Mainpage.html')
		except PersonalInfo.DoesNotExist as e:
			messages.success(request,'Email and  Password Invalid!!')
	return render(request,'login_sbp.html')

def Logout_sbp(request):
	try:
		del request.session['otc_email']
	except:
		return render(request,'Mainpage.html')
	return render(request,'Mainpage.html')

def Effects_Survey(request):
	if request.method == "POST":
		Vac_Immunity = request.POST['Vac_Immunity']
		Vaccination_Category = request.POST['Vaccination_Category']
		Physical_mild_Effects = request.POST['Physical_mild_Effects']
		Physical_Serious_Effects = request.POST['Physical_Serious_Effects']
		Mental_Effects = request.POST['Mental_Effects']
		Trigger_Past_Illness = request.POST['Trigger_Past_Illness']
		Experience_Effects = request.POST['Experience_Effects']
		date_created = request.POST['date_created']
		
		vaccinations_Takein = Vaccinations_Takein(
		Vac_Immunity = Vac_Immunity,
		Vaccination_Category = Vaccination_Category,
		Physical_mild_Effects = Physical_mild_Effects,
		Physical_Serious_Effects = Physical_Serious_Effects,
		Mental_Effects = Mental_Effects,
		Trigger_Past_Illness = Trigger_Past_Illness,
		Experience_Effects = Experience_Effects,
		date_created = date_created,
		)
		vaccinations_Takein.save()
		#return redirect('/')
		messages.info(request,"Thankyou for Answering your Experiences")

	else:
		return render(request,'report_effects_surv.html')

	vac_effects = Vaccinations_Takein.objects.all()

	return render(request,'report_effects_surv.html',{'vac_effects': vac_effects})



def Delete_effects(request,sbpid):
	vaccinations_Takein= Vaccinations_Takein.objects.get(id = sbpid)
	vaccinations_Takein.delete()
	#message.info(request,"SBP MEMBER DELETED")

	return render(request,'SBP_deleted.html')


def Edit_effects(request,sbpid):
	sbp_edit_effects =Vaccinations_Takein.objects.get(id = sbpid)
	vac_effects = Vaccinations_Takein.objects.all()
	return render(request,'report_effects_surv.html',{'sbp_edit_effects':sbp_edit_effects,
		'vac_effects':vac_effects,
		})


def Update_effects(request,sbpid):
	vac_effects = Vaccinations_Takein.objects.get(id = sbpid)
	vac_effects.Vac_Immunity = request.POST['Vac_Immunity']
	vac_effects.Vaccination_Category = request.POST['Vaccination_Category']
	vac_effects.Physical_mild_Effects = request.POST['Physical_mild_Effects']
	vac_effects.Physical_Serious_Effects = request.POST['Physical_Serious_Effects']
	vac_effects.Mental_Effects = request.POST['Mental_Effects']
	vac_effects.Trigger_Past_Illness = request.POST['Trigger_Past_Illness']
	vac_effects.Experience_Effects = request.POST['Experience_Effects']
	vac_effects.date_created = request.POST['date_created']
	vac_effects.save()
	messages.info(request,"Vaccines Effects Survey  Succesful Updated")
	return redirect('Vaccine_effect_updated')




def Positive_Survey(request):
	if request.method == "POST":
		# Vac_positive_Immunity = request.POST['Vac_positive_Immunity']
		# Vaccination_Types_Category = request.POST['Vaccination_Types_Category']
		Vaccination_Effects_Felt = request.POST['Vaccination_Effects_Felt']
		Vaccination_Effects_Body_Felt = request.POST['Vaccination_Effects_Body_Felt']
		Positive_effects_one = request.POST['Positive_effects_one']
		Positive_effects_two = request.POST['Positive_effects_two']
		date_created_vaccine = request.POST['date_created_vaccine']
		
		positive_effects = Positive_effects(
		# Vac_positive_Immunity = Vac_positive_Immunity,
		# Vaccination_Types_Category = Vaccination_Types_Category,
		Vaccination_Effects_Felt =Vaccination_Effects_Felt,
		Vaccination_Effects_Body_Felt = Vaccination_Effects_Body_Felt,
		Positive_effects_one =Positive_effects_one,
		Positive_effects_two = Positive_effects_two,
		date_created_vaccine = date_created_vaccine,
		)
		positive_effects.save()
		#return redirect('/')
		messages.info(request,"THANK YOU WE GLAD TO HEAR THAT, GOD BLESS!! ")

	else:
		return render(request,'positive_effects_phy_ment.html')

	vac_positive_effects = Positive_effects.objects.all()

	return render(request,'positive_effects_phy_ment.html',{'vac_positive_effects': vac_positive_effects})

def Delete_pos_effects(request,sbpid):
	positive_effect =Positive_effects.objects.get(id = sbpid)
	positive_effect.delete()
	#message.info(request,"SBP MEMBER DELETED")
	#return redirect('')

	return render(request,'SBP_deleted.html')

def Edit_pos_effects(request,sbpid):
	sbp_edit_pos_effects =Positive_effects.objects.get(id = sbpid)
	vac_positive_effects = Positive_effects.objects.all()
	return render(request,'positive_effects_phy_ment.html',{'sbp_edit_pos_effects':sbp_edit_pos_effects,
		'vac_positive_effects':vac_positive_effects,
		})



def Update_pos_effects(request,sbpid):
	vac_positive_effects =Positive_effects.objects.get(id = sbpid)
	vac_positive_effects.Vaccination_Effects_Felt = request.POST['Vaccination_Effects_Felt']
	vac_positive_effects.Vaccination_Effects_Body_Felt = request.POST['Vaccination_Effects_Body_Felt']
	vac_positive_effects.Positive_effects_one = request.POST['Positive_effects_one']
	vac_positive_effects.Positive_effects_two = request.POST['Positive_effects_two']
	vac_positive_effects.date_created_vaccine = request.POST['date_created_vaccine']
	vac_positive_effects.save()
	messages.info(request,"Vaccines Effects Survey  Succesful Updated")
	return redirect('Vaccine_effect_updated')

def Notvac_survey(request):
	if request.method == "POST":
		Concern_One = request.POST['Concern_One']
		Concern_Two = request.POST['Concern_Two']
		Concern_Three = request.POST['Concern_Three']
		Other_Concern_Reason = request.POST['Other_Concern_Reason']
		vaccinations_not_decide = Vaccinations_not_decide(
		Concern_One = Concern_One,
		Concern_Two = Concern_Two,
		Concern_Three = Concern_Three,
		Other_Concern_Reason =Other_Concern_Reason,
		)
		vaccinations_not_decide.save()
		#return redirect('/')
		messages.info(request,"Thankyou for Answering your Concerns , We gladly to hear That")

	else:
		return render(request,'reports_notvac_surv.html')

	concern_vaccinated = Vaccinations_not_decide.objects.all()

	return render(request,'reports_notvac_surv.html',{'concern_vaccinated': concern_vaccinated})

def Delete_concerns(request,sbpid):
	vaccinations_not_decide= Vaccinations_not_decide.objects.get(id = sbpid)
	vaccinations_not_decide.delete()
	#message.info(request,"SBP MEMBER DELETED")
	#return redirect('')

	return render(request,'SBP_deleted.html')
	#return render(request,'table_vaceff.html')


def Edit_concerns(request,sbpid):
	sbp_edit_concerns =Vaccinations_not_decide.objects.get(id = sbpid)
	concern_vaccinated = Vaccinations_not_decide.objects.all()
	return render(request,'reports_notvac_surv.html',{'sbp_edit_concerns':sbp_edit_concerns,
		'concern_vaccinated':concern_vaccinated,
		})


def Update_concerns(request,sbpid):
	concern_vaccinated = Vaccinations_not_decide.objects.get(id = sbpid)
	concern_vaccinated.Concern_One = request.POST['Concern_One']
	concern_vaccinated.Concern_Two = request.POST['Concern_Two']
	concern_vaccinated.Concern_Three = request.POST['Concern_Three']
	concern_vaccinated.Other_Concern_Reason = request.POST['Other_Concern_Reason']
	concern_vaccinated.save()
	#messages.info(request,"SBP Member Succesful Update")
	return redirect('Vaccine_effect_updated')





def DashBoard(request):
	sbp_members_dashboard =PersonalInfo.objects.all()\


	vac_effects_db = Vaccinations_Takein.objects.all()
	vac_positive_db = Positive_effects.objects.all()
	concern_effects_db = Vaccinations_not_decide.objects.all()
	total_members_dashboard= sbp_members_dashboard.count()
	total_vac_effects_db = vac_effects_db.count()
	total_vac_positive_db = vac_positive_db.count()
	total_concern_effects_db = concern_effects_db.count()


	pfizer_count = vac_effects_db.filter(Vaccination_Category='Pfizer').count()
	AstraZeneca_count = vac_effects_db.filter(Vaccination_Category='AstraZeneca').count()
	Sinovac_count = vac_effects_db.filter(Vaccination_Category='Sinovac').count()
	Sputnik_count = vac_effects_db.filter(Vaccination_Category='Sputnik').count()
	Johnsons_Janssen_count = vac_effects_db.filter(Vaccination_Category='Johnsons Janssen').count()
	BioTech_count = vac_effects_db.filter(Vaccination_Category='BioTech').count()
	Moderna_count = vac_effects_db.filter(Vaccination_Category='Moderna').count()
	return render(request,'dashboard.html',{'sbp_members_dashboard':sbp_members_dashboard,
		'vac_effects_db':vac_effects_db,
		'total_members_dashboard':total_members_dashboard,
		'total_vac_effects_db':total_vac_effects_db,
		'total_concern_effects_db':total_concern_effects_db,
		'total_vac_positive_db': total_vac_positive_db,
		'pfizer_count':pfizer_count,
		'AstraZeneca_count':AstraZeneca_count,
		'Sinovac_count':Sinovac_count,
		'Sputnik_count':Sputnik_count,
		'Johnsons_Janssen_count':Johnsons_Janssen_count,
		'BioTech_count':BioTech_count,
		'Moderna_count':Moderna_count
		})



def Table_Vaccination(request):
	vac_effects = Vaccinations_Takein.objects.all()

	paginator = Paginator(vac_effects,3)
	sbp_effects_page_number = request.GET.get('page')
	vac_effects = paginator.get_page(sbp_effects_page_number)

	vac_positive_effects = Positive_effects.objects.all()
	paginator = Paginator(vac_positive_effects,3)
	sbp_effects_page_number = request.GET.get('page')
	vac_positive_effects = paginator.get_page(sbp_effects_page_number)
	
	otc_members =PersonalInfo.objects.all()
	paginator = Paginator(otc_members,3)
	sbp_effects_page_number = request.GET.get('page')
	otc_members = paginator.get_page(sbp_effects_page_number)



	concern_vaccinated = Vaccinations_not_decide.objects.all()

	paginator = Paginator(concern_vaccinated,3)
	sbp_effects_page_number = request.GET.get('page')
	concern_vaccinated = paginator.get_page(sbp_effects_page_number)


	return render(request,'table_vaceff.html',{
		'vac_effects': vac_effects,
		'otc_members': otc_members,
		'concern_vaccinated': concern_vaccinated,
		'vac_positive_effects':vac_positive_effects,}
		)



def Feed_back(request):
	if request.method == "POST":
		Message_response = request.POST['Message_response']

		message_sbp = Message_sbp(
		Message_response = Message_response,
		)
		message_sbp.save()
		#return redirect('/')
		messages.info(request,"Thank you for contacting us with your concern or comment.")

	else:
		return render(request,'feedback.html')

	message_sbp = Message_sbp.objects.all()

	return render(request,'feedback.html',{
		'message_sbp':message_sbp}
		)


def Delete_message(request,sbpid):
	message_sbp= Message_sbp.objects.get(id = sbpid)
	message_sbp.delete()
	#message.info(request,"SBP MEMBER DELETED")
	#return redirect('feedback')

	#return render(request,'table_feedback.html')
	return render(request,'SBP_deleted.html')



def Edit_message(request,sbpid):
	sbp_edit_message =Message_sbp.objects.get(id = sbpid)
	message_sbp = Message_sbp.objects.all()
	return render(request,'feedback.html',{'sbp_edit_message':sbp_edit_message,
		'message_sbp ':message_sbp,
		})


def Update_message(request,sbpid):
	message_sbp = Message_sbp.objects.get(id = sbpid)
	message_sbp.Message_response = request.POST['Message_response']
	
	message_sbp.save()
	#messages.info(request,"SBP Member Succesful Update")
	return redirect('Vaccine_effect_updated')

def Comments_Message(request):
	message_sbp = Message_sbp.objects.all()
	return render(request,'table_feedback.html',{'message_sbp': message_sbp,}
		)


def Vaccine_effect_updated(request):
	return render(request,'Vaccine_effect_updated.html')


def SBP_deleted(request):
	return render(request,'SBP_deleted')