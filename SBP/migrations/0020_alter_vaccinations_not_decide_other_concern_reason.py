# Generated by Django 4.0.4 on 2022-06-20 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SBP', '0019_alter_personalinfo_otc_sex_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccinations_not_decide',
            name='Other_Concern_Reason',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
