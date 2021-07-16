# Generated by Django 3.2.5 on 2021-07-16 22:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WakeUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('goal_hour', models.IntegerField(default=0)),
                ('goal_minute', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('start_days', models.IntegerField(default=0)),
                ('continuity_days', models.IntegerField(default=0)),
                ('success_days', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Certify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('fulfill_hour', models.IntegerField(default=0)),
                ('fulfill_minute', models.IntegerField(default=0)),
                ('achievement', models.BooleanField(default=False)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wakeup.wakeup')),
            ],
        ),
    ]
