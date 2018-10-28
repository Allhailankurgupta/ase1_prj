# Generated by Django 2.1.2 on 2018-10-28 16:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0011_auto_20181028_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='unique_code',
            field=models.CharField(db_index=True, help_text="A unique code for your question. between 3-15 characters. May contain only                                    lowercase characters and numbers. For example if the question name is 'Sorting Array',                                    you may name the code SORTARR", max_length=15, unique=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator('^[0-9a-z]*$', 'The Unique code can contain only small case alphabets and numbers ')], verbose_name='Unique Code'),
        ),
    ]