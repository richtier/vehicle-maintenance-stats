# Generated by Django 3.2.16 on 2022-10-17 11:55

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_document_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to=core.models.file_generate_upload_path),
        ),
    ]
