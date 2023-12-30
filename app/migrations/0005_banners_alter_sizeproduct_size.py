# Generated by Django 4.2.6 on 2023-12-30 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_imagage_brands_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banners/')),
                ('text', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='sizeproduct',
            name='size',
            field=models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('3XL', '3XL')], max_length=30, verbose_name='Size'),
        ),
    ]
