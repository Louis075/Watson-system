# Generated by Django 2.0 on 2019-01-09 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watsons', '0021_auto_20190109_2346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateField(blank=True, null=True)),
                ('end_time', models.DateField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
