# Generated by Django 4.0.3 on 2022-03-18 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_alter_record_adviser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='date',
            field=models.DateField(),
        ),
    ]
