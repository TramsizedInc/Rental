# Generated by Django 5.1 on 2025-03-24 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApartmentImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='apartment_images/')),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='user.room')),
            ],
            options={
                'verbose_name_plural': 'Apartment Images',
            },
        ),
        migrations.CreateModel(
            name='HouseImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='house_images/')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='user.house')),
            ],
            options={
                'verbose_name_plural': 'House Images',
            },
        ),
    ]
