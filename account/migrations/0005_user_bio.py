# Generated by Django 3.2.7 on 2021-09-14 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]