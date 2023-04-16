# Generated by Django 4.1.5 on 2023-03-27 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_title',
            new_name='task_name',
        ),
        migrations.RemoveField(
            model_name='task',
            name='task_desk',
        ),
        migrations.RemoveField(
            model_name='task',
            name='time',
        ),
        migrations.AddField(
            model_name='task',
            name='complated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='du_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')], default='L', max_length=1),
        ),
    ]
