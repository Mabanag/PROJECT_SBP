# Generated by Django 4.0.4 on 2022-06-06 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SBP', '0002_rename_otc_address_personalinfo_sbp_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='SBP_status',
            field=models.CharField(choices=[('Student', 'Student'), ('Employed', 'Employed'), ('Nonemployed', 'Nonemployed')], max_length=200, null=True),
        ),
    ]