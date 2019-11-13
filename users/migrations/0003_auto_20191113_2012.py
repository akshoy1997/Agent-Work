# Generated by Django 2.2.6 on 2019-11-13 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191106_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='details',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='target',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='details',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='follow_up_date',
            field=models.DateField(null=True, verbose_name='Follow Up Date'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='status',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='date',
            field=models.DateField(null=True, verbose_name='Conversation Date'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='time',
            field=models.TimeField(null=True, verbose_name='Conversation Time'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='venue',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]