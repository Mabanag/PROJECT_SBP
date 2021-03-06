# Generated by Django 4.0.4 on 2022-06-16 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SBP', '0006_vaccinations_not_decide'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration_Online_Schedule_Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_Fname', models.CharField(max_length=200, null=True)),
                ('reg_Lname', models.CharField(max_length=200, null=True)),
                ('reg_Age', models.CharField(max_length=200, null=True)),
                ('reg_barangay', models.CharField(max_length=200, null=True)),
                ('reg_munincipality', models.CharField(max_length=200, null=True)),
                ('otc_sex', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200, null=True)),
                ('Online_Form_Four', models.CharField(choices=[('Lung Disease', 'Lung Disease'), ('Heart Disease', 'Heart Disease'), ('Asthma', 'Asthma'), ('Kidney Disease', 'Kidney Disease'), ('Diabetes', 'Diabetes'), ('Anemia', 'Anemia'), ('Blood Disorder', 'Blood Disorder'), ('None', 'None')], max_length=150, null=True)),
                ('Online_Form_Five', models.CharField(choices=[('Cancer', 'Leukemia'), ('Lyphoma', 'HIV/AIDS'), ('Transplant', 'Transplant'), ('Asplenia', 'Asplenia'), ('None', 'None')], max_length=100, null=True)),
                ('Online_Form_Six', models.CharField(max_length=100, null=True)),
                ('Online_Form_Seven', models.CharField(choices=[('Fever', 'Fever'), ('Cold', 'Cold'), ('Cough', 'Cough'), ('Shortness Of Breath', 'Shortness Of Breath'), ('Sore Throats', 'Soar Throats')], max_length=100, null=True)),
                ('Vaccine_Take', models.CharField(choices=[('1st Dose', '1st Dose'), ('2nd Dose', '2nd Dose'), ('First Booster', 'First Booster'), ('Second Booster', 'Second Booster')], max_length=200, null=True)),
                ('Emergency_Full_Name', models.CharField(max_length=100, null=True)),
                ('Emergency_Email', models.EmailField(max_length=100, null=True)),
                ('Emergency_Contact_Number', models.CharField(max_length=100, null=True)),
                ('Emergency_Relation', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
