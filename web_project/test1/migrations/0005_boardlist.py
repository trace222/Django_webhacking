# Generated by Django 2.1 on 2019-12-06 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0004_auto_20191005_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boardlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('introduction', models.TextField()),
            ],
        ),
    ]
