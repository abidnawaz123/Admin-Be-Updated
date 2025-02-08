# Generated by Django 5.1.5 on 2025-02-08 12:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_delete_ticketheadings'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadmodel',
            name='lead_team',
            field=models.ManyToManyField(related_name='lead_team', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projectmodel',
            name='assigned_employee',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticketmodel',
            name='assigned_employee',
            field=models.ManyToManyField(related_name='assigned_employee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='EmployeeModel',
        ),
    ]
