# Generated by Django 4.2.1 on 2023-06-09 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tendering', '0005_itemprice_extra_field_alter_itemprice_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemprice',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Vendor',
        ),
    ]