# Generated by Django 2.2.6 on 2019-11-13 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191113_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeadHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('deleted_date', models.DateTimeField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('status', models.CharField(max_length=10, null=True)),
                ('registered_phone_nos', models.CharField(max_length=100, null=True)),
                ('more_details', models.CharField(max_length=1000, null=True)),
                ('reason', models.CharField(max_length=100, null=True)),
                ('detailed_reason', models.CharField(max_length=1000, null=True)),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lead_history', to='users.Lead')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]