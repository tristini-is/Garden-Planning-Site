# Generated by Django 4.2.6 on 2023-11-06 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden_app', '0004_alter_plant_box'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThemeChanger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_dark', models.BooleanField(default=False)),
            ],
        ),
    ]
