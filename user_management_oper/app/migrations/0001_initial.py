# Generated by Django 2.2.13 on 2021-09-13 08:30

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_register',
            fields=[
                ('Username', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('desig', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30, validators=[app.models.main])),
            ],
        ),
    ]