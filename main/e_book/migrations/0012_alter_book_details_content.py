# Generated by Django 4.2.6 on 2023-10-15 11:22

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_book', '0011_alter_book_chapter_chapter_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_details',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='welcome', null=True),
        ),
    ]
