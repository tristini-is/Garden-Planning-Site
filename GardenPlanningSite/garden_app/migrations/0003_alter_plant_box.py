# Generated by Django 4.2.6 on 2023-11-04 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garden_app', '0002_plant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='box',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='garden_app.planter'),
        ),
    ]
