# Generated by Django 2.2.6 on 2019-10-08 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('devices', '0002_sonoffremotesocket'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('ENRS', 'Enable Remote Socket'), ('DIRS', 'Disable Remote Socket'), ('SECO', 'Set LED Strip Color')], max_length=4)),
                ('parameters', models.CharField(blank=True, max_length=50)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.Device')),
            ],
        ),
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('actions', models.ManyToManyField(to='automation.Action')),
            ],
        ),
    ]
