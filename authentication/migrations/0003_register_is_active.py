# Generated by Django 4.2.4 on 2023-08-12 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_rename_signup_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
