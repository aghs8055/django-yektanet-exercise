# Generated by Django 2.2 on 2021-10-20 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celery_app', '0006_auto_20211019_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayreport',
            name='day',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dayreport',
            name='month',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dayreport',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='hourreport',
            name='day',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='hourreport',
            name='hour',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='hourreport',
            name='month',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='hourreport',
            name='year',
            field=models.IntegerField(),
        ),
    ]
