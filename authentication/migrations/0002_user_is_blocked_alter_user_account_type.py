# Generated by Django 4.2.4 on 2023-09-01 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_blocked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='account_type',
            field=models.CharField(choices=[('user', 'User'), ('doctor', 'Doctor'), ('admin', 'Admin')], max_length=20),
        ),
    ]
