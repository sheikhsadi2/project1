# Generated by Django 4.2.6 on 2023-10-15 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_book', '0010_alter_book_details_page_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_chapter',
            name='chapter_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]