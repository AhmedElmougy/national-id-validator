# Generated by Django 3.1.3 on 2021-02-27 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NationalId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('national_id', models.IntegerField(unique=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('place_of_birth', models.CharField(default='', max_length=16)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='', max_length=1)),
            ],
        ),
    ]
