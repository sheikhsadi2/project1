# Generated by Django 4.2.6 on 2023-10-13 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pro_pic',
            field=models.ImageField(blank=True, null=True, upload_to='pro_pic/'),
        ),
    ]
