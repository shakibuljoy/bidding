# Generated by Django 4.2.1 on 2023-06-09 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tendering', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemprice',
            name='extra_field',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itemprice',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]