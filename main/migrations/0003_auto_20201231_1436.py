# Generated by Django 3.1.4 on 2020-12-31 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_blog_data_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_data',
            name='category',
            field=models.CharField(choices=[('cooking', 'cooking'), ('ent', 'ent')], default='', max_length=200),
        ),
    ]
