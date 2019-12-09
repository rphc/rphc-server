# Generated by Django 2.2.6 on 2019-10-08 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('automation', '0002_disableremotesocketaction_enableremotesocketaction_setledstripcoloraction'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='action',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='disableremotesocketaction',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='enableremotesocketaction',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='setledstripcoloraction',
            options={'base_manager_name': 'objects'},
        ),
        migrations.RemoveField(
            model_name='action',
            name='action',
        ),
        migrations.RemoveField(
            model_name='action',
            name='device',
        ),
        migrations.RemoveField(
            model_name='action',
            name='parameters',
        ),
        migrations.RemoveField(
            model_name='disableremotesocketaction',
            name='id',
        ),
        migrations.RemoveField(
            model_name='enableremotesocketaction',
            name='id',
        ),
        migrations.RemoveField(
            model_name='setledstripcoloraction',
            name='id',
        ),
        migrations.AddField(
            model_name='action',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_automation.action_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='disableremotesocketaction',
            name='action_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='automation.Action'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enableremotesocketaction',
            name='action_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='automation.Action'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setledstripcoloraction',
            name='action_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='automation.Action'),
            preserve_default=False,
        ),
    ]
