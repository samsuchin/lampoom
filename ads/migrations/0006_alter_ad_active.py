# Generated by Django 3.2.7 on 2021-09-30 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_remove_ad_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
