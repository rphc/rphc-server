# Generated by Django 2.2.6 on 2019-10-08 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0004_action_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='name',
        ),
    ]
