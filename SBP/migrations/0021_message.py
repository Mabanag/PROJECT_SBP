# Generated by Django 4.0.4 on 2022-06-21 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SBP', '0020_alter_vaccinations_not_decide_other_concern_reason'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message_response', models.TextField(default=' ')),
                ('Individuals', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SBP.personalinfo')),
            ],
        ),
    ]
