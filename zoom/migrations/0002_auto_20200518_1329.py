# Generated by Django 3.0.5 on 2020-05-18 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zoom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zoom',
            name='link',
            field=models.CharField(max_length=255),
        ),
    ]
