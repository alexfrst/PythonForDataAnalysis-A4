# Generated by Django 3.1.5 on 2021-01-09 21:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModelInterface', '0003_auto_20210109_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='current_assets',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='record',
            name='financial_expenses',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='record',
            name='inventory',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='record',
            name='operating_expenses',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='record',
            name='profit_on_operating_activities',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='record',
            name='profit_on_sales',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='record',
            name='sales_of_the_previous_year',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='record',
            name='sales_of_the_year',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='record',
            name='short_term_liabilities',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='record',
            name='total_assets',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='record',
            name='total_liabilities',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='record',
            name='year',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]