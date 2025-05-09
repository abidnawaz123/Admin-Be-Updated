# Generated by Django 5.1.5 on 2025-02-02 11:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_assigned_users_projectmodel_assigned_lead'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TicketModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=300)),
                ('number', models.IntegerField()),
                ('description', models.TextField(max_length=1000)),
                ('status', models.CharField(max_length=100)),
                ('priority', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='low', max_length=10)),
                ('time_estimated', models.DateTimeField(auto_now_add=True)),
                ('date_to_complete', models.DateTimeField(auto_now_add=True)),
                ('extra_fields', models.JSONField(default=dict)),
                ('assigned_lead', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.leadmodel')),
                ('tags', models.ManyToManyField(related_name='ticket_tags', to='api.tickettags')),
            ],
        ),
        migrations.CreateModel(
            name='TicketHeadings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ticket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.ticketmodel')),
            ],
        ),
    ]
