# Generated by Django 3.1.5 on 2021-01-10 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModelInterface', '0006_auto_20210109_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('X1', models.FloatField(default=0)),
                ('X2', models.FloatField(default=0)),
                ('X3', models.FloatField(default=0)),
                ('X4', models.FloatField(default=0)),
                ('X5', models.FloatField(default=0)),
                ('X6', models.FloatField(default=0)),
                ('X7', models.FloatField(default=0)),
                ('X8', models.FloatField(default=0)),
                ('X9', models.FloatField(default=0)),
                ('X10', models.FloatField(default=0)),
                ('X11', models.FloatField(default=0)),
                ('X12', models.FloatField(default=0)),
                ('Class', models.CharField(max_length=15)),
                ('Year', models.IntegerField()),
            ],
        ),
    ]
