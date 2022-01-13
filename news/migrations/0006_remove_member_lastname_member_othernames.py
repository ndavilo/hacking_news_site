# Generated by Django 4.0 on 2022-01-12 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_rename_members_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='lastname',
        ),
        migrations.AddField(
            model_name='member',
            name='othernames',
            field=models.CharField(default='Other names here', max_length=50),
        ),
    ]
