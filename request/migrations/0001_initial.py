# Generated by Django 3.2.4 on 2021-06-09 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DurationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submition_date', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SingleDayRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submition_date', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateField()),
                ('availability', models.BooleanField()),
                ('shift', models.CharField(max_length=10)),
                ('note', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
