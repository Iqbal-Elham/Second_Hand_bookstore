# Generated by Django 3.2.15 on 2022-12-25 19:58

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
            name='user_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('gender', models.CharField(default='Male', max_length=10)),
                ('phone_num', models.CharField(blank=True, max_length=15, null=True)),
                ('whatsapp_num', models.CharField(blank=True, max_length=15, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/profiles/')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
