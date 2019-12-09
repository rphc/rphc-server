# Generated by Django 2.2.6 on 2019-10-08 16:04

import colorful.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_sonoffremotesocket'),
        ('automation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetLedStripColorAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', colorful.fields.RGBColorField()),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.Device')),
            ],
        ),
        migrations.CreateModel(
            name='EnableRemoteSocketAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.Device')),
            ],
        ),
        migrations.CreateModel(
            name='DisableRemoteSocketAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.Device')),
            ],
        ),
    ]
