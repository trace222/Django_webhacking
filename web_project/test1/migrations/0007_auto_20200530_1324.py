# Generated by Django 2.1 on 2020-05-30 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0006_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='candidate',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='poll',
        ),
        migrations.DeleteModel(
            name='Candidate',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Poll',
        ),
    ]
