# Generated by Django 2.0 on 2019-01-02 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watsons', '0003_auto_20190102_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CO', 'Cosmetic'), ('SA', 'Snacks'), ('CR', 'Care Product')], default='CO', max_length=2),
        ),
    ]