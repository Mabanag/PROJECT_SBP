# Generated by Django 4.0.4 on 2022-06-17 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SBP', '0011_vaccinations_takein_date_vaccines'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaccinations_takein',
            name='Intakedosevaccine_info',
        ),
        migrations.RemoveField(
            model_name='vaccinations_takein',
            name='classofvaccine_info',
        ),
        migrations.DeleteModel(
            name='Vaccinations_ClassofVaccine',
        ),
        migrations.DeleteModel(
            name='Vaccinations_Doseofvaccineintake',
        ),
    ]