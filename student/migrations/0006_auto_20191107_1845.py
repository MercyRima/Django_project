# Generated by Django 2.2.1 on 2019-11-07 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20191107_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(blank=True, null=True, related_name='Students', to='course.Course'),
        ),
    ]
