# Generated by Django 3.2.19 on 2023-06-14 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_tests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uniquelogin',
            name='unique_string',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]