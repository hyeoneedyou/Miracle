# Generated by Django 3.2.5 on 2021-07-23 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certify',
            name='created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='health',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
