# Generated by Django 2.2.1 on 2019-11-07 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20191017_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(blank=True, null=True, related_name='Student', to='course.Course'),
        ),
    ]
