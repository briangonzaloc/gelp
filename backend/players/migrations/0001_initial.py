# Generated by Django 2.2.4 on 2019-09-04 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('birthday', models.DateField(null=True)),
                ('weight', models.FloatField(null=True)),
                ('height', models.FloatField(null=True)),
            ],
        ),
    ]
