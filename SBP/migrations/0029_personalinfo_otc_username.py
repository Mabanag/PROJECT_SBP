# Generated by Django 4.0.4 on 2022-06-27 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SBP', '0028_personalinfo_otc_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='otc_username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]