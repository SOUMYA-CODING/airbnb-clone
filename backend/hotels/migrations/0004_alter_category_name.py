# Generated by Django 4.0.4 on 2022-08-29 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
