# Generated by Django 4.0.4 on 2022-06-24 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SBP', '0025_remove_positive_effects_positive_effects_three'),
    ]

    operations = [
        migrations.AddField(
            model_name='positive_effects',
            name='date_created_vaccine',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
