# Generated by Django 3.0.5 on 2020-05-22 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20200522_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='completion',
            field=models.CharField(default='0%', max_length=10),
        ),
    ]
