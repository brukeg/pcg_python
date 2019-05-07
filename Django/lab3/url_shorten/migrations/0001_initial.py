# Generated by Django 2.0.13 on 2019-05-02 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.URLField(max_length=500, unique=True)),
                ('short', models.CharField(max_length=8)),
            ],
        ),
    ]