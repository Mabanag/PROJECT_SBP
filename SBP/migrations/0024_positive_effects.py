# Generated by Django 4.0.4 on 2022-06-24 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SBP', '0023_alter_vaccinations_takein_physical_serious_effects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Positive_effects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vac_positive_Immunity', models.CharField(choices=[('1st Dose', '1st Dose'), ('2nd Dose', '2nd Dose'), ('First Booster', 'First Booster'), ('Second Booster', 'Second Booster')], max_length=200, null=True)),
                ('Vaccination_Types_Category', models.CharField(choices=[('Pfizer', 'Pfizer'), ('AstraZeneca', 'AstraZeneca'), ('Sinovac', 'Sinovac'), ('Sputnik', 'Sputnik'), ('Johnsons Janssen', 'Johnsons Janssen'), ('BioTech', 'BioTech'), ('Moderna', 'Moderna')], max_length=200, null=True)),
                ('Vaccination_Effects_Felt', models.CharField(choices=[('Happy', 'Happy'), ('Reliefs and Gratitude', 'Reliefs and Gratitude'), ('freedom with care', 'freedom with care'), ('Being Active', 'Being Active'), ('None', 'None')], max_length=200, null=True)),
                ('Vaccination_Effects_Body_Felt', models.CharField(choices=[('Feeling energized', 'Feeling energized'), ('Doing work lightly(mas magaan ang mga gawain)', 'Doing work lightly(mas magaan ang mga gawain)'), ('Cherish little things about life', 'Cherish little things about life'), ('No more sleeping deprivation ( hindi na hirap sa pagtulog)', 'No more sleeping deprivation ( hindi na hirap sa pagtulog)'), ('None', 'None')], max_length=200, null=True)),
                ('Positive_effects_one', models.CharField(max_length=200, null=True)),
                ('Positive_effects_two', models.CharField(max_length=200, null=True)),
                ('Positive_effects_three', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]