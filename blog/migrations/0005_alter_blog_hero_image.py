# Generated by Django 4.2 on 2023-04-08 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='hero_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]