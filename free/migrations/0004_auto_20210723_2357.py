# Generated by Django 3.2.5 on 2021-07-23 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('free', '0003_alter_certify_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certify',
            name='created',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='free',
            name='created',
            field=models.DateField(),
        ),
    ]
