# Generated by Django 3.2.7 on 2021-09-18 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('read', '0017_magazine_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazine',
            name='custom_art_editor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='magazine',
            name='custom_issue_editor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
