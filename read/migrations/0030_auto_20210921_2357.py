# Generated by Django 3.2.7 on 2021-09-21 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('read', '0029_auto_20210920_0650'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artwork',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='magazine',
            name='works',
            field=models.ManyToManyField(blank=True, related_name='magazines', to='read.Work'),
        ),
    ]