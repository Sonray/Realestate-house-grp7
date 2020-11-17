# Generated by Django 3.1.3 on 2020-11-12 11:07

import cloudinary.models
# Generated by Django 2.2.5 on 2020-11-12 06:12
# Generated by Django 3.1.3 on 2020-11-12 11:43

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
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='photos')),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=300)),
                ('category', models.CharField(max_length=300)),
                ('location', models.CharField(max_length=300)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='houses', to=settings.AUTH_USER_MODEL)),
            
            name='Inquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120)),
                ('location', models.CharField(blank=True, max_length=60)),
                ('contact', models.EmailField(blank=True, max_length=100)),
                ('message', models.TextField(blank=True, max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='inquire', to=settings.AUTH_USER_MODEL)),
            ],
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_id', models.IntegerField(default=0)),
                ('image', models.ImageField(default='', upload_to='images/')),
                ('bio', models.TextField(blank=True, default='My Bio', max_length=500)),
                ('name', models.CharField(blank=True, max_length=120)),
                ('location', models.CharField(blank=True, max_length=60)),
                ('email', models.CharField(blank=True, max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
