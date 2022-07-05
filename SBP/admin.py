from django.contrib import admin
from .models import *


admin.site.register(PersonalInfo)
# admin.site.register(Vaccinations_Doseofvaccineintake) 
# admin.site.register(Vaccinations_ClassofVaccine) 
admin.site.register(Vaccinations_Takein)
admin.site.register(Vaccinations_not_decide) 
admin.site.register(Positive_effects)
# admin.site.register(Registration_Online_Schedule_Form)
