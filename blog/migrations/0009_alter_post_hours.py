# Generated by Django 3.2.9 on 2021-12-02 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='hours',
            field=models.DateTimeField(),
        ),
    ]